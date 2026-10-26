# dea:metric-rack-power-density

Candidate Performance Metric record for **Rack Power Density** (RPD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-rack-power-density`
- **Name:** Rack Power Density
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RPD

## 2. Definition

Rack Power Density (RPD) addresses the utilization or availability of capacity and is a fixture of data centers & cloud infrastructure reporting. It is defined as Power Draw / Rack; the result is stated in ratio (x:1 or x). In Technology, it is a recognized element of the standard performance toolkit. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Values outside the intended band, on either side, warrant investigation.

## Formula

```
RPD = Power Draw / Rack
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** data_centers_cloud_infrastructure
- **Sector:** technology

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2141 (batch 6)
