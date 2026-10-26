# dea:metric-data-throughput-per-user

Candidate Performance Metric record for **Data Throughput per User** (DTPU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-throughput-per-user`
- **Name:** Data Throughput per User
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DTPU

## 2. Definition

Within Telecom Network Operations, Data Throughput per User (DTPU) is used to gauge the quality of outputs and outcomes. It is computed as Total Data Delivered / Active Users, expressed in ratio (x:1 or x). Its use is concentrated in Telecommunications. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Total Data Delivered / Active Users
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** telecom_network_operations
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 864 (batch 3)
