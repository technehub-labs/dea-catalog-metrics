# dea:metric-empty-miles-rate

Candidate Performance Metric record for **Empty Miles Rate** (EMR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-empty-miles-rate`
- **Name:** Empty Miles Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** EMR

## 2. Definition

Empty Miles Rate (EMR) measures how efficiently resources are converted into outputs in the Logistics & Transportation domain. Its calculation is Empty Miles / Total Miles, measured in percent (%). Its value drives prioritization and resource reallocation among competing initiatives. Lower values are better; each reduction is an improvement. It originates from and is most used in Logistics practice.

## 3. Context

Measures the share of driven miles running without a paying load. It matters because empty miles burn fuel and driver hours while generating zero revenue. It can be cut cosmetically by reclassifying repositioning as load-related or refusing far pickups that would actually serve customers. Read with Load Factor and Cost per Mile to confirm that lower empty miles improve real network economics.

## Formula

```
EMR = Empty Miles / Total Miles
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** logistics_transportation
- **Sector:** logistics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 196 (batch 1)
