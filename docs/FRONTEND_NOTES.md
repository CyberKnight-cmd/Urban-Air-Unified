# 🎨 Frontend Integration & Dashboard Guide

This document is an exhaustive manual tailored for Frontend Engineers (React, Next.js, Vue, or Vanilla JS) tasked with building the Urban Air Intelligence dashboard. It provides detailed code snippets, architectural paradigms, and integration strategies to harness the full power of the FastAPI backend.

The backend is specifically engineered to provide rich, visual data formats (GeoJSON, Audio URLs, Percentage Maps) to reduce frontend computational overhead.

---

## 1. Geospatial Map Integration (GeoJSON Plumes)

The `/api/v1/ml/predict` endpoint returns a `dispersion_plume` object. This is a strictly formatted `GeoJSON` Feature of type `Polygon`. It is mathematically calculated by the backend based on live wind speed and wind direction from Open-Meteo.

### Mapbox GL JS Integration Example
If you are using Mapbox to render the interactive city map, you can seamlessly add the plume as a transparent red smoke layer.

```javascript
// Assuming `apiResponse` is the JSON from /api/v1/ml/predict
const plumeGeoJSON = apiResponse.dispersion_plume;

map.on('load', () => {
    // 1. Add the GeoJSON object as a source
    map.addSource('pollution-plume', {
        type: 'geojson',
        data: plumeGeoJSON
    });

    // 2. Add a polygon fill layer to render the smoke
    map.addLayer({
        id: 'plume-fill',
        type: 'fill',
        source: 'pollution-plume',
        paint: {
            'fill-color': '#ff4d4d', // Toxic red
            'fill-opacity': 0.4      // Semi-transparent
        }
    });

    // 3. Add an outline for visual clarity
    map.addLayer({
        id: 'plume-outline',
        type: 'line',
        source: 'pollution-plume',
        paint: {
            'line-color': '#cc0000',
            'line-width': 2
        }
    });
});
```
**Why this matters:** The plume will dynamically point in the correct direction (e.g., blowing West if there is an East wind) and will stretch further across the city if the wind speed is high. This creates a massive "Wow Factor" for hackathon judges.

---

## 2. Interactive Voice Response (IVR) Audio Player

The `/api/v1/health/health-advisory` endpoint asynchronously generates a high-quality, British-accented Neural text-to-speech file using `edge-tts` and saves it to the backend's static mount.

### React Integration Example
You can build a "Play Health Advisory" button component that streams the MP3 directly from the server.

```jsx
import React, { useState, useRef } from 'react';

const AdvisoryAudioPlayer = ({ audioUrl }) => {
  const [isPlaying, setIsPlaying] = useState(false);
  const audioRef = useRef(new Audio(audioUrl));

  const togglePlay = () => {
    if (isPlaying) {
      audioRef.current.pause();
    } else {
      audioRef.current.play();
    }
    setIsPlaying(!isPlaying);
  };

  // Listen for track completion to reset button state
  audioRef.current.onended = () => setIsPlaying(false);

  return (
    <div className="audio-card p-4 bg-gray-800 rounded-lg shadow-lg">
      <h3 className="text-white mb-2">🔊 Listen to Local Advisory</h3>
      <button 
        onClick={togglePlay}
        className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded"
      >
        {isPlaying ? '⏸ Pause' : '▶️ Play Warning'}
      </button>
    </div>
  );
};
```
*Note:* Ensure your frontend allows media autoplay if you want to trigger this automatically on severe AQI events.

---

## 3. Data Visualization (Source Attribution)

The Machine Learning NMF algorithm breaks down the pollution into percentage vectors. 
`attribution: { "traffic_pct": 0.6, "industrial_pct": 0.2, ... }`

### Recharts Integration Example
To visualize this, a Doughnut chart is highly recommended.

```jsx
import { PieChart, Pie, Cell, Tooltip, Legend } from 'recharts';

const SourceAttributionChart = ({ attributionData }) => {
  // Map the JSON response to Recharts format
  const data = [
    { name: 'Traffic', value: attributionData.traffic_pct * 100 },
    { name: 'Industrial', value: attributionData.industrial_pct * 100 },
    { name: 'Biomass', value: attributionData.biomass_pct * 100 },
    { name: 'Solvents/VOC', value: attributionData.solvent_voc_pct * 100 },
  ];

  const COLORS = ['#FF8042', '#00C49F', '#FFBB28', '#0088FE'];

  return (
    <PieChart width={400} height={400}>
      <Pie
        data={data}
        cx={200}
        cy={200}
        innerRadius={60}
        outerRadius={80}
        paddingAngle={5}
        dataKey="value"
      >
        {data.map((entry, index) => (
          <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
        ))}
      </Pie>
      <Tooltip formatter={(value) => `${value.toFixed(1)}%`} />
      <Legend />
    </PieChart>
  );
};
```

---

## 4. Editing the NoSQL Mock Data

To demonstrate Multi-City Analytics without setting up a MongoDB cluster, we use `TinyDB`.
If you need to tweak the numbers (e.g., make Bangalore's AQI look worse for a specific presentation slide):
1. Open the `analytics_database.json` file in the root of the backend directory.
2. Manually edit the JSON values (e.g., change `"current_avg_aqi": 85` to `350`).
3. Save the file.
4. Refresh your React dashboard. The API will instantly serve the new data! No server restart required.
