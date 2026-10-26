# dea:metric-time-to-data-insight

Candidate Performance Metric record for **Time to Data Insight** (TTDI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-time-to-data-insight`
- **Name:** Time to Data Insight
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TTDI

## 2. Definition

Time to Data Insight (TTDI) captures how efficiently resources are converted into outputs for organizations tracking data management & analytics. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Days from Question Raised to Analytical Answer Delivered; the result is stated in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures elapsed time from question or event to delivered analytical insight. It matters because decision value decays fast, so slow analytics is late analytics. It can be gamed by shipping shallow descriptive answers fast while deep questions wait. Read with Analytics Adoption Rate and Data Freshness trends to check speed is paired with decision-grade quality.

## Formula

```
Days from Question Raised to Analytical Answer Delivered
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** data_management_analytics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 342 (batch 1)
