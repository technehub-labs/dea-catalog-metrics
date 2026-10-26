# dea:metric-power-usage-effectiveness

Candidate Performance Metric record for **Power Usage Effectiveness** (PUE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-power-usage-effectiveness`
- **Name:** Power Usage Effectiveness
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PUE

## 2. Definition

Power Usage Effectiveness (PUE) captures how efficiently resources are converted into outputs for organizations tracking data center & cloud operations. It is defined as Total Facility Power / IT Equipment Power; the result is stated in ratio (x:1 or x). Its trend is watched by senior leadership as an early signal of structural performance shifts. Lower values are better; each reduction is an improvement. In Technology & data centers, it is a recognized element of the standard performance toolkit.

## 3. Context

PUE, defined by The Green Grid (2007), is total facility energy divided by IT equipment energy - the standard efficiency yardstick for data centers. A PUE of 1.0 is the theoretical ideal (all power reaches IT); legacy facilities often exceed 2.0, modern hyperscale sites run near 1.1, and anything above 1.5 warrants scrutiny of cooling and power distribution. PUE is annualized and weather-dependent, so compare like climates and seasons - a winter PUE flatters any facility.

## Formula

```
PUE = Total Facility Power / IT Equipment Power
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** data_center_cloud_operations
- **Sector:** technology_data_centers

## Attribution

- **Source credit:** The Green Grid, 2007

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1088 (batch 4)
