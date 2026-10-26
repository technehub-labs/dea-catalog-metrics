# dea:metric-query-p95-latency

Candidate Performance Metric record for **Query P95 Latency** (QPS95) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-query-p95-latency`
- **Name:** Query P95 Latency
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** QPS95

## 2. Definition

Query P95 Latency (QPS95) captures the quality of outputs and outcomes for organizations tracking database & data platform operations. It is computed as 95th Percentile Database Query Execution Time, expressed in milliseconds (ms). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Lower values are better; each reduction is an improvement. Its use is concentrated in Software.

## Formula

```
QPS95 = 95th Percentile Database Query Execution Time
```

## Unit

- **Unit reference:** `dea:unit-millisecond`
- **Unit:** millisecond
- **Unit label (as published):** milliseconds (ms)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** database_data_platform_operations
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3226 (batch 7)
