# dea:metric-de-icing-cycle-compliance

Candidate Performance Metric record for **De-Icing Cycle Compliance** (DICC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-de-icing-cycle-compliance`
- **Name:** De-Icing Cycle Compliance
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DICC

## 2. Definition

Within Airport Operations (Deep Dive), De-Icing Cycle Compliance (DICC) is used to gauge exposure to adverse outcomes. Its calculation is De-Icing within Holdover Time / Applications, measured in percent (%). It originates from and is most used in Aviation practice. It provides the day-to-day signal that a process is running as designed. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
De-Icing within Holdover Time / Applications
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airport_operations_deep_dive
- **Sector:** aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2279 (batch 6)
