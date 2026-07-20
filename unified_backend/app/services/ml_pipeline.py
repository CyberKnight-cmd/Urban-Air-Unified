"""
End-to-end inference pipeline: raw recent readings -> attribution % + forecast.
This is the function your LangGraph agent calls directly.
"""

import os
import joblib
import numpy as np
import pandas as pd

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../Urban-Air-Intelligence"))
ATTR_DIR = os.path.join(BASE_DIR, "01_source_attribution/attribution_outputs")
FCST_DIR = os.path.join(BASE_DIR, "02_aqi_forecasting/forecasting_outputs")

# ---------- Load all artifacts once at import time ----------
nmf_model = joblib.load(os.path.join(ATTR_DIR, "models", "nmf_model.pkl"))
nmf_scale_factors = joblib.load(os.path.join(ATTR_DIR, "models", "nmf_scale_factors.pkl"))
nmf_required = joblib.load(os.path.join(ATTR_DIR, "models", "nmf_feature_order.pkl"))
factor_mapping = joblib.load(os.path.join(ATTR_DIR, "models", "factor_mapping.pkl"))
fire_scale = joblib.load(os.path.join(ATTR_DIR, "models", "fire_scale.pkl"))
max_reconstruction_error = joblib.load(os.path.join(ATTR_DIR, "models", "max_reconstruction_error.pkl"))

xgb_models = {h: joblib.load(os.path.join(FCST_DIR, "models", f"xgb_pm25_{h}.pkl")) for h in ["1h", "24h", "48h"]}
feature_cols = joblib.load(os.path.join(FCST_DIR, "models", "feature_cols.pkl"))

PM = "PM2.5 (µg/m³)"


def load_imputer(station, base_dir):
    path = os.path.join(base_dir, "imputers", f"missforest_{station}.pkl")
    if not os.path.exists(path):
        path = os.path.join(base_dir, "imputers", "missforest_global.pkl")
    return joblib.load(path)


def impute_latest(recent_df, station, model_cols, base_dir):
    """Impute missing values in the most recent row using the station's
    (or global fallback) fitted imputer."""
    imputer_bundle = load_imputer(station, base_dir)
    imputer, usable_cols = imputer_bundle["imputer"], imputer_bundle["cols"]
    cols_present = [c for c in model_cols if c in recent_df.columns]
    try:
        recent_df.loc[:, cols_present] = imputer.transform(recent_df[cols_present])
    except ValueError as e:
        # MissForest throws an error if the dataframe is already 100% clean
        if "at least one missing value" in str(e):
            pass
        else:
            raise
    
    return recent_df


def engineer_features(recent_df):
    """recent_df: sorted-by-Timestamp DataFrame for ONE station, >=168h of
    history recommended (needed for lag_48h / roll_24h / diff_24h). Returns
    the fully-engineered latest row as a single-row DataFrame."""
    d = recent_df.sort_values("Timestamp").copy()

    for lag in [1, 3, 6, 12, 24, 48]:
        d[f"PM25_lag_{lag}h"] = d[PM].shift(lag)
    d["PM25_roll_mean_24h"] = d[PM].shift(1).rolling(24).mean()
    d["PM25_roll_std_24h"] = d[PM].shift(1).rolling(24).std()
    d["PM25_diff_1h"] = d[PM].diff(1)
    d["PM25_diff_3h"] = d[PM].diff(3)
    d["PM25_diff_24h"] = d[PM].diff(24)

    d["hour"] = d["Timestamp"].dt.hour
    d["month"] = d["Timestamp"].dt.month
    d["hour_sin"] = np.sin(2 * np.pi * d["hour"] / 24)
    d["hour_cos"] = np.cos(2 * np.pi * d["hour"] / 24)
    d["month_sin"] = np.sin(2 * np.pi * d["month"] / 12)
    d["month_cos"] = np.cos(2 * np.pi * d["month"] / 12)
    d["calm_wind"] = (d["WS (m/s)"] < 2).astype(int)

    return d.iloc[[-1]]  # latest row only, now fully engineered


def compute_attribution(latest_row, fire_data_available=True):
    X_raw = latest_row[nmf_required].clip(lower=0)
    X_scaled = X_raw / nmf_scale_factors
    W = nmf_model.transform(X_scaled)
    H = nmf_model.components_
    factor_pct = (W / W.sum(axis=1, keepdims=True))[0]

    factor_names = [f"factor_{i}" for i in range(len(factor_pct))]
    pct_by_factor = dict(zip(factor_names, factor_pct))

    traffic_factor_pct = pct_by_factor[factor_mapping["traffic"]]
    industrial_pct = pct_by_factor[factor_mapping["industrial"]]
    voc_pct = pct_by_factor[factor_mapping["voc"]]

    fire_count = latest_row["fire_count_far_upwind"].values[0] if "fire_count_far_upwind" in latest_row else 0
    fire_signal = np.log1p(fire_count) / fire_scale
    fire_signal = np.clip(fire_signal, 0, 1)

    biomass_pct = traffic_factor_pct * fire_signal
    traffic_pct = traffic_factor_pct * (1 - fire_signal)

    total = traffic_pct + biomass_pct + industrial_pct + voc_pct
    result = {
        "traffic_pct": traffic_pct / total,
        "biomass_pct": biomass_pct / total,
        "industrial_pct": industrial_pct / total,
        "solvent_voc_pct": voc_pct / total,
    }

    reconstruction = W @ H
    error = np.linalg.norm(X_scaled.values - reconstruction, axis=1)[0]
    confidence = 1 - (error / max_reconstruction_error)
    if not fire_data_available:
        confidence *= 0.5  # discount confidence when fire data is missing (e.g. 2025 gap)

    result["confidence"] = float(np.clip(confidence, 0, 1))
    return result


def compute_forecast(latest_row):
    forecasts = {}
    row_features = latest_row[feature_cols]
    for h in ["1h", "24h", "48h"]:
        forecasts[h] = float(xgb_models[h].predict(row_features)[0])
    return forecasts


def run_pipeline(recent_df, station, fire_data_available=True, already_imputed=False):
    """
    recent_df:
        Raw dataframe containing recent history for ONE station.

    station:
        Station name.

    fire_data_available:
        Whether fire data exists for confidence calculation.

    already_imputed:
        If True, assumes the dataframe has already been passed through
        MissForest. Useful for batch inference so we don't repeatedly
        reload and run the imputer.
    """

    model_cols = [
        "PM2.5 (µg/m³)",
        "PM10 (µg/m³)",
        "NO2 (µg/m³)",
        "NOx (ppb)",
        "SO2 (µg/m³)",
        "CO (mg/m³)",
        "Benzene (µg/m³)",
        "Toluene (µg/m³)",
        "AT (°C)",
        "RH (%)",
        "WS (m/s)",
        "WD (deg)",
        "BP (mmHg)",
    ]

    d = recent_df.sort_values("Timestamp").copy()

    if not already_imputed:
        d = impute_latest(d, station, model_cols, ATTR_DIR)

    latest_row = engineer_features(d)
    attribution = compute_attribution(latest_row, fire_data_available)

    forecasts = compute_forecast(latest_row)

    return {
        "station": station,
        "timestamp": str(latest_row["Timestamp"].values[0]),
        "attribution": attribution,
        "forecast_pm25": forecasts,
    }


if __name__ == "__main__":
    # Quick smoke test - replace with a real recent slice from your test set
    print("Import this module and call run_pipeline(recent_df, station_name).")