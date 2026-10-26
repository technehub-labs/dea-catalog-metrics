# dea:metric-system-average-interruption-frequency-index

Candidate Performance Metric record for **System Average Interruption Frequency Index** (SAIFI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-system-average-interruption-frequency-index`
- **Name:** System Average Interruption Frequency Index
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SAIFI

## 2. Definition

Within Energy & Utilities, System Average Interruption Frequency Index (SAIFI) is used to gauge the quality of outputs and outcomes. The formula is Total Customer Interruptions / Total Customers Served - reported in ratio (x:1 or x). It is a standard measure in the Energy & utilities sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

The average number of sustained outages each customer experiences per year - the IEEE 1366 metric that, with SAIDI, defines reliability for distribution utilities and anchors the service-quality rules that regulators apply. Its strategic weight is regulatory economics: performance in defined percentiles against peer benchmarks sets the terms for rate cases in performance-based regimes, and utilities earn incentives or absorb penalties directly on this number. The diagnostic value is in the count-versus-duration split: high SAIFI with low SAIDI means many brief outages - switching operations, wildlife, weather - while low SAIFI with high SAIDI points to rarer, harder failures (underground cable, transformer) that need different investment. Major-event-day exclusion (per the IEEE convention) keeps storms from swamping the trend, which is what makes the index an asset-health signal rather than a weather report.

## Formula

```
Total Customer Interruptions / Total Customers Served
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** energy_utilities
- **Sector:** energy_utilities

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 436 (batch 1)
