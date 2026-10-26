# dea:metric-data-center-cooling-efficiency

Candidate Performance Metric record for **Data Center Cooling Efficiency** (DCCE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-center-cooling-efficiency`
- **Name:** Data Center Cooling Efficiency
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DCCE

## 2. Definition

Data Center Cooling Efficiency (DCCE) captures how efficiently resources are converted into outputs for organizations tracking data center & cloud operations. Its calculation is IT Load / Cooling Load, measured in ratio (x:1 or x). It originates from and is most used in Technology & data centers practice. Its value drives prioritization and resource reallocation among competing initiatives. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures cooling energy relative to IT load (such as PUE). It matters because cooling is the dominant non-IT energy cost and a direct sustainability metric. Partial utilization can flatter PUE while stranded capacity wastes capital. Read with Rack Space Utilization and Energy Cost per unit of compute to confirm efficiency is real at operating load.

## Formula

```
IT Load / Cooling Load
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** data_center_cloud_operations
- **Sector:** technology_data_centers

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1099 (batch 4)
