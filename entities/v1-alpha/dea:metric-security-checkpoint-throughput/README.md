# dea:metric-security-checkpoint-throughput

Candidate Performance Metric record for **Security Checkpoint Throughput** (SCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-security-checkpoint-throughput`
- **Name:** Security Checkpoint Throughput
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SCT

## 2. Definition

Security Checkpoint Throughput (SCT) addresses the utilization or availability of capacity and is a fixture of airport operations reporting. It is computed as Passengers Screened / Checkpoint Lane Hour, expressed in ratio (x:1 or x). Its use is concentrated in Airports. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
SCT = Passengers Screened / Checkpoint Lane Hour
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airport_operations
- **Sector:** airports

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1178 (batch 4)
