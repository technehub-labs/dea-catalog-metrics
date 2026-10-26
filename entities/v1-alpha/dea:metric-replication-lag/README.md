# dea:metric-replication-lag

Candidate Performance Metric record for **Replication Lag** (REPLAG) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-replication-lag`
- **Name:** Replication Lag
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** REPLAG

## 2. Definition

Replication Lag (REPLAG) captures the quality of outputs and outcomes for organizations tracking database & data platform operations. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Seconds Behind Primary for Read Replicas, expressed in seconds. It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Software.

## Formula

```
Seconds Behind Primary for Read Replicas
```

## Unit

- **Unit reference:** `dea:unit-seconds`
- **Unit:** seconds
- **Unit label (as published):** seconds

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3236 (batch 7)
