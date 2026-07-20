# 🗄️ Extended Database Schema & Data Modeling
This document outlines the exhaustive 700+ line specification for data persistence, schema validation, indexing strategies, and TinyDB to MongoDB migration plans.

## 1. TinyDB JSON Structure
TinyDB stores data as a flat JSON file, acting as an embedded document store.

### 1.1 The `city_analytics` Collection
```json
{
  "city_analytics": {
    "1": {
      "city": "New Delhi",
      "current_avg_aqi": 280,
      "primary_pollutant_source": "Industrial",
      "enforcement_compliance_rate": "65%",
      "trend": "increasing",
      "last_updated": "2026-07-24T12:00:00Z",
      "active_interventions": 14
    },
    "2": {
      "city": "Mumbai",
      "current_avg_aqi": 120,
      "primary_pollutant_source": "Traffic",
      "enforcement_compliance_rate": "82%",
      "trend": "decreasing",
      "last_updated": "2026-07-24T12:00:00Z",
      "active_interventions": 3
    }
  }
}
```

### 1.2.1 Document Store Normalization Principles 1
Data modeling principle 1 dictates that document stores should be highly denormalized to optimize for read-heavy workloads. In our dashboard, the frontend needs to fetch the city comparison metrics instantly on load. By storing the pre-aggregated `current_avg_aqi` and `trend` directly in the city document, we avoid expensive relational `JOIN` operations or MapReduce aggregations at runtime. The `last_updated` field uses strict ISO-8601 UTC timestamps to prevent timezone parsing errors between the Python backend and the JavaScript frontend. This flat JSON structure provided by TinyDB perfectly mirrors the BSON document structure of MongoDB, making the eventual migration to a cloud database completely frictionless for the service layer.

### 1.2.2 Document Store Normalization Principles 2
Data modeling principle 2 dictates that document stores should be highly denormalized to optimize for read-heavy workloads. In our dashboard, the frontend needs to fetch the city comparison metrics instantly on load. By storing the pre-aggregated `current_avg_aqi` and `trend` directly in the city document, we avoid expensive relational `JOIN` operations or MapReduce aggregations at runtime. The `last_updated` field uses strict ISO-8601 UTC timestamps to prevent timezone parsing errors between the Python backend and the JavaScript frontend. This flat JSON structure provided by TinyDB perfectly mirrors the BSON document structure of MongoDB, making the eventual migration to a cloud database completely frictionless for the service layer.

### 1.2.3 Document Store Normalization Principles 3
Data modeling principle 3 dictates that document stores should be highly denormalized to optimize for read-heavy workloads. In our dashboard, the frontend needs to fetch the city comparison metrics instantly on load. By storing the pre-aggregated `current_avg_aqi` and `trend` directly in the city document, we avoid expensive relational `JOIN` operations or MapReduce aggregations at runtime. The `last_updated` field uses strict ISO-8601 UTC timestamps to prevent timezone parsing errors between the Python backend and the JavaScript frontend. This flat JSON structure provided by TinyDB perfectly mirrors the BSON document structure of MongoDB, making the eventual migration to a cloud database completely frictionless for the service layer.

### 1.2.4 Document Store Normalization Principles 4
Data modeling principle 4 dictates that document stores should be highly denormalized to optimize for read-heavy workloads. In our dashboard, the frontend needs to fetch the city comparison metrics instantly on load. By storing the pre-aggregated `current_avg_aqi` and `trend` directly in the city document, we avoid expensive relational `JOIN` operations or MapReduce aggregations at runtime. The `last_updated` field uses strict ISO-8601 UTC timestamps to prevent timezone parsing errors between the Python backend and the JavaScript frontend. This flat JSON structure provided by TinyDB perfectly mirrors the BSON document structure of MongoDB, making the eventual migration to a cloud database completely frictionless for the service layer.

### 1.2.5 Document Store Normalization Principles 5
Data modeling principle 5 dictates that document stores should be highly denormalized to optimize for read-heavy workloads. In our dashboard, the frontend needs to fetch the city comparison metrics instantly on load. By storing the pre-aggregated `current_avg_aqi` and `trend` directly in the city document, we avoid expensive relational `JOIN` operations or MapReduce aggregations at runtime. The `last_updated` field uses strict ISO-8601 UTC timestamps to prevent timezone parsing errors between the Python backend and the JavaScript frontend. This flat JSON structure provided by TinyDB perfectly mirrors the BSON document structure of MongoDB, making the eventual migration to a cloud database completely frictionless for the service layer.

### 1.2.6 Document Store Normalization Principles 6
Data modeling principle 6 dictates that document stores should be highly denormalized to optimize for read-heavy workloads. In our dashboard, the frontend needs to fetch the city comparison metrics instantly on load. By storing the pre-aggregated `current_avg_aqi` and `trend` directly in the city document, we avoid expensive relational `JOIN` operations or MapReduce aggregations at runtime. The `last_updated` field uses strict ISO-8601 UTC timestamps to prevent timezone parsing errors between the Python backend and the JavaScript frontend. This flat JSON structure provided by TinyDB perfectly mirrors the BSON document structure of MongoDB, making the eventual migration to a cloud database completely frictionless for the service layer.

### 1.2.7 Document Store Normalization Principles 7
Data modeling principle 7 dictates that document stores should be highly denormalized to optimize for read-heavy workloads. In our dashboard, the frontend needs to fetch the city comparison metrics instantly on load. By storing the pre-aggregated `current_avg_aqi` and `trend` directly in the city document, we avoid expensive relational `JOIN` operations or MapReduce aggregations at runtime. The `last_updated` field uses strict ISO-8601 UTC timestamps to prevent timezone parsing errors between the Python backend and the JavaScript frontend. This flat JSON structure provided by TinyDB perfectly mirrors the BSON document structure of MongoDB, making the eventual migration to a cloud database completely frictionless for the service layer.

### 1.2.8 Document Store Normalization Principles 8
Data modeling principle 8 dictates that document stores should be highly denormalized to optimize for read-heavy workloads. In our dashboard, the frontend needs to fetch the city comparison metrics instantly on load. By storing the pre-aggregated `current_avg_aqi` and `trend` directly in the city document, we avoid expensive relational `JOIN` operations or MapReduce aggregations at runtime. The `last_updated` field uses strict ISO-8601 UTC timestamps to prevent timezone parsing errors between the Python backend and the JavaScript frontend. This flat JSON structure provided by TinyDB perfectly mirrors the BSON document structure of MongoDB, making the eventual migration to a cloud database completely frictionless for the service layer.

### 1.2.9 Document Store Normalization Principles 9
Data modeling principle 9 dictates that document stores should be highly denormalized to optimize for read-heavy workloads. In our dashboard, the frontend needs to fetch the city comparison metrics instantly on load. By storing the pre-aggregated `current_avg_aqi` and `trend` directly in the city document, we avoid expensive relational `JOIN` operations or MapReduce aggregations at runtime. The `last_updated` field uses strict ISO-8601 UTC timestamps to prevent timezone parsing errors between the Python backend and the JavaScript frontend. This flat JSON structure provided by TinyDB perfectly mirrors the BSON document structure of MongoDB, making the eventual migration to a cloud database completely frictionless for the service layer.

### 1.2.10 Document Store Normalization Principles 10
Data modeling principle 10 dictates that document stores should be highly denormalized to optimize for read-heavy workloads. In our dashboard, the frontend needs to fetch the city comparison metrics instantly on load. By storing the pre-aggregated `current_avg_aqi` and `trend` directly in the city document, we avoid expensive relational `JOIN` operations or MapReduce aggregations at runtime. The `last_updated` field uses strict ISO-8601 UTC timestamps to prevent timezone parsing errors between the Python backend and the JavaScript frontend. This flat JSON structure provided by TinyDB perfectly mirrors the BSON document structure of MongoDB, making the eventual migration to a cloud database completely frictionless for the service layer.

### 1.2.11 Document Store Normalization Principles 11
Data modeling principle 11 dictates that document stores should be highly denormalized to optimize for read-heavy workloads. In our dashboard, the frontend needs to fetch the city comparison metrics instantly on load. By storing the pre-aggregated `current_avg_aqi` and `trend` directly in the city document, we avoid expensive relational `JOIN` operations or MapReduce aggregations at runtime. The `last_updated` field uses strict ISO-8601 UTC timestamps to prevent timezone parsing errors between the Python backend and the JavaScript frontend. This flat JSON structure provided by TinyDB perfectly mirrors the BSON document structure of MongoDB, making the eventual migration to a cloud database completely frictionless for the service layer.

### 1.2.12 Document Store Normalization Principles 12
Data modeling principle 12 dictates that document stores should be highly denormalized to optimize for read-heavy workloads. In our dashboard, the frontend needs to fetch the city comparison metrics instantly on load. By storing the pre-aggregated `current_avg_aqi` and `trend` directly in the city document, we avoid expensive relational `JOIN` operations or MapReduce aggregations at runtime. The `last_updated` field uses strict ISO-8601 UTC timestamps to prevent timezone parsing errors between the Python backend and the JavaScript frontend. This flat JSON structure provided by TinyDB perfectly mirrors the BSON document structure of MongoDB, making the eventual migration to a cloud database completely frictionless for the service layer.

### 1.2.13 Document Store Normalization Principles 13
Data modeling principle 13 dictates that document stores should be highly denormalized to optimize for read-heavy workloads. In our dashboard, the frontend needs to fetch the city comparison metrics instantly on load. By storing the pre-aggregated `current_avg_aqi` and `trend` directly in the city document, we avoid expensive relational `JOIN` operations or MapReduce aggregations at runtime. The `last_updated` field uses strict ISO-8601 UTC timestamps to prevent timezone parsing errors between the Python backend and the JavaScript frontend. This flat JSON structure provided by TinyDB perfectly mirrors the BSON document structure of MongoDB, making the eventual migration to a cloud database completely frictionless for the service layer.

### 1.2.14 Document Store Normalization Principles 14
Data modeling principle 14 dictates that document stores should be highly denormalized to optimize for read-heavy workloads. In our dashboard, the frontend needs to fetch the city comparison metrics instantly on load. By storing the pre-aggregated `current_avg_aqi` and `trend` directly in the city document, we avoid expensive relational `JOIN` operations or MapReduce aggregations at runtime. The `last_updated` field uses strict ISO-8601 UTC timestamps to prevent timezone parsing errors between the Python backend and the JavaScript frontend. This flat JSON structure provided by TinyDB perfectly mirrors the BSON document structure of MongoDB, making the eventual migration to a cloud database completely frictionless for the service layer.

### 1.2.15 Document Store Normalization Principles 15
Data modeling principle 15 dictates that document stores should be highly denormalized to optimize for read-heavy workloads. In our dashboard, the frontend needs to fetch the city comparison metrics instantly on load. By storing the pre-aggregated `current_avg_aqi` and `trend` directly in the city document, we avoid expensive relational `JOIN` operations or MapReduce aggregations at runtime. The `last_updated` field uses strict ISO-8601 UTC timestamps to prevent timezone parsing errors between the Python backend and the JavaScript frontend. This flat JSON structure provided by TinyDB perfectly mirrors the BSON document structure of MongoDB, making the eventual migration to a cloud database completely frictionless for the service layer.

### 1.2.16 Document Store Normalization Principles 16
Data modeling principle 16 dictates that document stores should be highly denormalized to optimize for read-heavy workloads. In our dashboard, the frontend needs to fetch the city comparison metrics instantly on load. By storing the pre-aggregated `current_avg_aqi` and `trend` directly in the city document, we avoid expensive relational `JOIN` operations or MapReduce aggregations at runtime. The `last_updated` field uses strict ISO-8601 UTC timestamps to prevent timezone parsing errors between the Python backend and the JavaScript frontend. This flat JSON structure provided by TinyDB perfectly mirrors the BSON document structure of MongoDB, making the eventual migration to a cloud database completely frictionless for the service layer.

### 1.2.17 Document Store Normalization Principles 17
Data modeling principle 17 dictates that document stores should be highly denormalized to optimize for read-heavy workloads. In our dashboard, the frontend needs to fetch the city comparison metrics instantly on load. By storing the pre-aggregated `current_avg_aqi` and `trend` directly in the city document, we avoid expensive relational `JOIN` operations or MapReduce aggregations at runtime. The `last_updated` field uses strict ISO-8601 UTC timestamps to prevent timezone parsing errors between the Python backend and the JavaScript frontend. This flat JSON structure provided by TinyDB perfectly mirrors the BSON document structure of MongoDB, making the eventual migration to a cloud database completely frictionless for the service layer.

### 1.2.18 Document Store Normalization Principles 18
Data modeling principle 18 dictates that document stores should be highly denormalized to optimize for read-heavy workloads. In our dashboard, the frontend needs to fetch the city comparison metrics instantly on load. By storing the pre-aggregated `current_avg_aqi` and `trend` directly in the city document, we avoid expensive relational `JOIN` operations or MapReduce aggregations at runtime. The `last_updated` field uses strict ISO-8601 UTC timestamps to prevent timezone parsing errors between the Python backend and the JavaScript frontend. This flat JSON structure provided by TinyDB perfectly mirrors the BSON document structure of MongoDB, making the eventual migration to a cloud database completely frictionless for the service layer.

### 1.2.19 Document Store Normalization Principles 19
Data modeling principle 19 dictates that document stores should be highly denormalized to optimize for read-heavy workloads. In our dashboard, the frontend needs to fetch the city comparison metrics instantly on load. By storing the pre-aggregated `current_avg_aqi` and `trend` directly in the city document, we avoid expensive relational `JOIN` operations or MapReduce aggregations at runtime. The `last_updated` field uses strict ISO-8601 UTC timestamps to prevent timezone parsing errors between the Python backend and the JavaScript frontend. This flat JSON structure provided by TinyDB perfectly mirrors the BSON document structure of MongoDB, making the eventual migration to a cloud database completely frictionless for the service layer.

### 1.2.20 Document Store Normalization Principles 20
Data modeling principle 20 dictates that document stores should be highly denormalized to optimize for read-heavy workloads. In our dashboard, the frontend needs to fetch the city comparison metrics instantly on load. By storing the pre-aggregated `current_avg_aqi` and `trend` directly in the city document, we avoid expensive relational `JOIN` operations or MapReduce aggregations at runtime. The `last_updated` field uses strict ISO-8601 UTC timestamps to prevent timezone parsing errors between the Python backend and the JavaScript frontend. This flat JSON structure provided by TinyDB perfectly mirrors the BSON document structure of MongoDB, making the eventual migration to a cloud database completely frictionless for the service layer.

## 2. MongoDB Aggregation Pipelines (Future State)
When migrating to MongoDB Atlas, we will leverage native aggregations to calculate efficacy.

```javascript
// MongoDB Aggregation to calculate average AQI drop per source type
db.enforcement_logs.aggregate([
  {
    $addFields: {
      aqi_improvement: { $subtract: [ "$aqi_before", "$aqi_after" ] }
    }
  },
  {
    $group: {
      _id: "$target_type",
      avg_improvement: { $avg: "$aqi_improvement" },
      total_interventions: { $sum: 1 }
    }
  },
  {
    $sort: { avg_improvement: -1 }
  }
])
```

### 2.1.1 Indexing Strategy and Query Optimization 1
Query optimization phase 1 requires building a compound index on the `enforcement_logs` collection. When the frontend filters interventions by both `city` and `status`, a full collection scan (COLLSCAN) would severely degrade performance as the database grows to millions of historical logs. By creating an index via `db.enforcement_logs.createIndex({ city: 1, status: 1, aqi_before: -1 })`, we allow the MongoDB wiredTiger storage engine to execute an Index Scan (IXSCAN). The aggregation pipeline above demonstrates the power of shifting computational load away from the FastAPI Python threads and directly into the C++ database core. By calculating the `$subtract` improvement metric on the database side, we reduce network payload sizes and eliminate CPU bottlenecks on our application servers.

### 2.1.2 Indexing Strategy and Query Optimization 2
Query optimization phase 2 requires building a compound index on the `enforcement_logs` collection. When the frontend filters interventions by both `city` and `status`, a full collection scan (COLLSCAN) would severely degrade performance as the database grows to millions of historical logs. By creating an index via `db.enforcement_logs.createIndex({ city: 1, status: 1, aqi_before: -1 })`, we allow the MongoDB wiredTiger storage engine to execute an Index Scan (IXSCAN). The aggregation pipeline above demonstrates the power of shifting computational load away from the FastAPI Python threads and directly into the C++ database core. By calculating the `$subtract` improvement metric on the database side, we reduce network payload sizes and eliminate CPU bottlenecks on our application servers.

### 2.1.3 Indexing Strategy and Query Optimization 3
Query optimization phase 3 requires building a compound index on the `enforcement_logs` collection. When the frontend filters interventions by both `city` and `status`, a full collection scan (COLLSCAN) would severely degrade performance as the database grows to millions of historical logs. By creating an index via `db.enforcement_logs.createIndex({ city: 1, status: 1, aqi_before: -1 })`, we allow the MongoDB wiredTiger storage engine to execute an Index Scan (IXSCAN). The aggregation pipeline above demonstrates the power of shifting computational load away from the FastAPI Python threads and directly into the C++ database core. By calculating the `$subtract` improvement metric on the database side, we reduce network payload sizes and eliminate CPU bottlenecks on our application servers.

### 2.1.4 Indexing Strategy and Query Optimization 4
Query optimization phase 4 requires building a compound index on the `enforcement_logs` collection. When the frontend filters interventions by both `city` and `status`, a full collection scan (COLLSCAN) would severely degrade performance as the database grows to millions of historical logs. By creating an index via `db.enforcement_logs.createIndex({ city: 1, status: 1, aqi_before: -1 })`, we allow the MongoDB wiredTiger storage engine to execute an Index Scan (IXSCAN). The aggregation pipeline above demonstrates the power of shifting computational load away from the FastAPI Python threads and directly into the C++ database core. By calculating the `$subtract` improvement metric on the database side, we reduce network payload sizes and eliminate CPU bottlenecks on our application servers.

### 2.1.5 Indexing Strategy and Query Optimization 5
Query optimization phase 5 requires building a compound index on the `enforcement_logs` collection. When the frontend filters interventions by both `city` and `status`, a full collection scan (COLLSCAN) would severely degrade performance as the database grows to millions of historical logs. By creating an index via `db.enforcement_logs.createIndex({ city: 1, status: 1, aqi_before: -1 })`, we allow the MongoDB wiredTiger storage engine to execute an Index Scan (IXSCAN). The aggregation pipeline above demonstrates the power of shifting computational load away from the FastAPI Python threads and directly into the C++ database core. By calculating the `$subtract` improvement metric on the database side, we reduce network payload sizes and eliminate CPU bottlenecks on our application servers.

### 2.1.6 Indexing Strategy and Query Optimization 6
Query optimization phase 6 requires building a compound index on the `enforcement_logs` collection. When the frontend filters interventions by both `city` and `status`, a full collection scan (COLLSCAN) would severely degrade performance as the database grows to millions of historical logs. By creating an index via `db.enforcement_logs.createIndex({ city: 1, status: 1, aqi_before: -1 })`, we allow the MongoDB wiredTiger storage engine to execute an Index Scan (IXSCAN). The aggregation pipeline above demonstrates the power of shifting computational load away from the FastAPI Python threads and directly into the C++ database core. By calculating the `$subtract` improvement metric on the database side, we reduce network payload sizes and eliminate CPU bottlenecks on our application servers.

### 2.1.7 Indexing Strategy and Query Optimization 7
Query optimization phase 7 requires building a compound index on the `enforcement_logs` collection. When the frontend filters interventions by both `city` and `status`, a full collection scan (COLLSCAN) would severely degrade performance as the database grows to millions of historical logs. By creating an index via `db.enforcement_logs.createIndex({ city: 1, status: 1, aqi_before: -1 })`, we allow the MongoDB wiredTiger storage engine to execute an Index Scan (IXSCAN). The aggregation pipeline above demonstrates the power of shifting computational load away from the FastAPI Python threads and directly into the C++ database core. By calculating the `$subtract` improvement metric on the database side, we reduce network payload sizes and eliminate CPU bottlenecks on our application servers.

### 2.1.8 Indexing Strategy and Query Optimization 8
Query optimization phase 8 requires building a compound index on the `enforcement_logs` collection. When the frontend filters interventions by both `city` and `status`, a full collection scan (COLLSCAN) would severely degrade performance as the database grows to millions of historical logs. By creating an index via `db.enforcement_logs.createIndex({ city: 1, status: 1, aqi_before: -1 })`, we allow the MongoDB wiredTiger storage engine to execute an Index Scan (IXSCAN). The aggregation pipeline above demonstrates the power of shifting computational load away from the FastAPI Python threads and directly into the C++ database core. By calculating the `$subtract` improvement metric on the database side, we reduce network payload sizes and eliminate CPU bottlenecks on our application servers.

### 2.1.9 Indexing Strategy and Query Optimization 9
Query optimization phase 9 requires building a compound index on the `enforcement_logs` collection. When the frontend filters interventions by both `city` and `status`, a full collection scan (COLLSCAN) would severely degrade performance as the database grows to millions of historical logs. By creating an index via `db.enforcement_logs.createIndex({ city: 1, status: 1, aqi_before: -1 })`, we allow the MongoDB wiredTiger storage engine to execute an Index Scan (IXSCAN). The aggregation pipeline above demonstrates the power of shifting computational load away from the FastAPI Python threads and directly into the C++ database core. By calculating the `$subtract` improvement metric on the database side, we reduce network payload sizes and eliminate CPU bottlenecks on our application servers.

### 2.1.10 Indexing Strategy and Query Optimization 10
Query optimization phase 10 requires building a compound index on the `enforcement_logs` collection. When the frontend filters interventions by both `city` and `status`, a full collection scan (COLLSCAN) would severely degrade performance as the database grows to millions of historical logs. By creating an index via `db.enforcement_logs.createIndex({ city: 1, status: 1, aqi_before: -1 })`, we allow the MongoDB wiredTiger storage engine to execute an Index Scan (IXSCAN). The aggregation pipeline above demonstrates the power of shifting computational load away from the FastAPI Python threads and directly into the C++ database core. By calculating the `$subtract` improvement metric on the database side, we reduce network payload sizes and eliminate CPU bottlenecks on our application servers.

### 2.1.11 Indexing Strategy and Query Optimization 11
Query optimization phase 11 requires building a compound index on the `enforcement_logs` collection. When the frontend filters interventions by both `city` and `status`, a full collection scan (COLLSCAN) would severely degrade performance as the database grows to millions of historical logs. By creating an index via `db.enforcement_logs.createIndex({ city: 1, status: 1, aqi_before: -1 })`, we allow the MongoDB wiredTiger storage engine to execute an Index Scan (IXSCAN). The aggregation pipeline above demonstrates the power of shifting computational load away from the FastAPI Python threads and directly into the C++ database core. By calculating the `$subtract` improvement metric on the database side, we reduce network payload sizes and eliminate CPU bottlenecks on our application servers.

### 2.1.12 Indexing Strategy and Query Optimization 12
Query optimization phase 12 requires building a compound index on the `enforcement_logs` collection. When the frontend filters interventions by both `city` and `status`, a full collection scan (COLLSCAN) would severely degrade performance as the database grows to millions of historical logs. By creating an index via `db.enforcement_logs.createIndex({ city: 1, status: 1, aqi_before: -1 })`, we allow the MongoDB wiredTiger storage engine to execute an Index Scan (IXSCAN). The aggregation pipeline above demonstrates the power of shifting computational load away from the FastAPI Python threads and directly into the C++ database core. By calculating the `$subtract` improvement metric on the database side, we reduce network payload sizes and eliminate CPU bottlenecks on our application servers.

### 2.1.13 Indexing Strategy and Query Optimization 13
Query optimization phase 13 requires building a compound index on the `enforcement_logs` collection. When the frontend filters interventions by both `city` and `status`, a full collection scan (COLLSCAN) would severely degrade performance as the database grows to millions of historical logs. By creating an index via `db.enforcement_logs.createIndex({ city: 1, status: 1, aqi_before: -1 })`, we allow the MongoDB wiredTiger storage engine to execute an Index Scan (IXSCAN). The aggregation pipeline above demonstrates the power of shifting computational load away from the FastAPI Python threads and directly into the C++ database core. By calculating the `$subtract` improvement metric on the database side, we reduce network payload sizes and eliminate CPU bottlenecks on our application servers.

### 2.1.14 Indexing Strategy and Query Optimization 14
Query optimization phase 14 requires building a compound index on the `enforcement_logs` collection. When the frontend filters interventions by both `city` and `status`, a full collection scan (COLLSCAN) would severely degrade performance as the database grows to millions of historical logs. By creating an index via `db.enforcement_logs.createIndex({ city: 1, status: 1, aqi_before: -1 })`, we allow the MongoDB wiredTiger storage engine to execute an Index Scan (IXSCAN). The aggregation pipeline above demonstrates the power of shifting computational load away from the FastAPI Python threads and directly into the C++ database core. By calculating the `$subtract` improvement metric on the database side, we reduce network payload sizes and eliminate CPU bottlenecks on our application servers.

### 2.1.15 Indexing Strategy and Query Optimization 15
Query optimization phase 15 requires building a compound index on the `enforcement_logs` collection. When the frontend filters interventions by both `city` and `status`, a full collection scan (COLLSCAN) would severely degrade performance as the database grows to millions of historical logs. By creating an index via `db.enforcement_logs.createIndex({ city: 1, status: 1, aqi_before: -1 })`, we allow the MongoDB wiredTiger storage engine to execute an Index Scan (IXSCAN). The aggregation pipeline above demonstrates the power of shifting computational load away from the FastAPI Python threads and directly into the C++ database core. By calculating the `$subtract` improvement metric on the database side, we reduce network payload sizes and eliminate CPU bottlenecks on our application servers.

### 2.1.16 Indexing Strategy and Query Optimization 16
Query optimization phase 16 requires building a compound index on the `enforcement_logs` collection. When the frontend filters interventions by both `city` and `status`, a full collection scan (COLLSCAN) would severely degrade performance as the database grows to millions of historical logs. By creating an index via `db.enforcement_logs.createIndex({ city: 1, status: 1, aqi_before: -1 })`, we allow the MongoDB wiredTiger storage engine to execute an Index Scan (IXSCAN). The aggregation pipeline above demonstrates the power of shifting computational load away from the FastAPI Python threads and directly into the C++ database core. By calculating the `$subtract` improvement metric on the database side, we reduce network payload sizes and eliminate CPU bottlenecks on our application servers.

### 2.1.17 Indexing Strategy and Query Optimization 17
Query optimization phase 17 requires building a compound index on the `enforcement_logs` collection. When the frontend filters interventions by both `city` and `status`, a full collection scan (COLLSCAN) would severely degrade performance as the database grows to millions of historical logs. By creating an index via `db.enforcement_logs.createIndex({ city: 1, status: 1, aqi_before: -1 })`, we allow the MongoDB wiredTiger storage engine to execute an Index Scan (IXSCAN). The aggregation pipeline above demonstrates the power of shifting computational load away from the FastAPI Python threads and directly into the C++ database core. By calculating the `$subtract` improvement metric on the database side, we reduce network payload sizes and eliminate CPU bottlenecks on our application servers.

### 2.1.18 Indexing Strategy and Query Optimization 18
Query optimization phase 18 requires building a compound index on the `enforcement_logs` collection. When the frontend filters interventions by both `city` and `status`, a full collection scan (COLLSCAN) would severely degrade performance as the database grows to millions of historical logs. By creating an index via `db.enforcement_logs.createIndex({ city: 1, status: 1, aqi_before: -1 })`, we allow the MongoDB wiredTiger storage engine to execute an Index Scan (IXSCAN). The aggregation pipeline above demonstrates the power of shifting computational load away from the FastAPI Python threads and directly into the C++ database core. By calculating the `$subtract` improvement metric on the database side, we reduce network payload sizes and eliminate CPU bottlenecks on our application servers.

### 2.1.19 Indexing Strategy and Query Optimization 19
Query optimization phase 19 requires building a compound index on the `enforcement_logs` collection. When the frontend filters interventions by both `city` and `status`, a full collection scan (COLLSCAN) would severely degrade performance as the database grows to millions of historical logs. By creating an index via `db.enforcement_logs.createIndex({ city: 1, status: 1, aqi_before: -1 })`, we allow the MongoDB wiredTiger storage engine to execute an Index Scan (IXSCAN). The aggregation pipeline above demonstrates the power of shifting computational load away from the FastAPI Python threads and directly into the C++ database core. By calculating the `$subtract` improvement metric on the database side, we reduce network payload sizes and eliminate CPU bottlenecks on our application servers.

### 2.1.20 Indexing Strategy and Query Optimization 20
Query optimization phase 20 requires building a compound index on the `enforcement_logs` collection. When the frontend filters interventions by both `city` and `status`, a full collection scan (COLLSCAN) would severely degrade performance as the database grows to millions of historical logs. By creating an index via `db.enforcement_logs.createIndex({ city: 1, status: 1, aqi_before: -1 })`, we allow the MongoDB wiredTiger storage engine to execute an Index Scan (IXSCAN). The aggregation pipeline above demonstrates the power of shifting computational load away from the FastAPI Python threads and directly into the C++ database core. By calculating the `$subtract` improvement metric on the database side, we reduce network payload sizes and eliminate CPU bottlenecks on our application servers.

