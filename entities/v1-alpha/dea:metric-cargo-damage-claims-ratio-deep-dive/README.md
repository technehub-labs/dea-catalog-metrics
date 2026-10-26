# dea:metric-cargo-damage-claims-ratio-deep-dive

Candidate Performance Metric record for **Cargo Damage Claims Ratio (Deep Dive)** (CDCR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cargo-damage-claims-ratio-deep-dive`
- **Name:** Cargo Damage Claims Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CDCR-D

## 2. Definition

Cargo Damage Claims Ratio (Deep Dive) (CDCR-D) addresses exposure to adverse outcomes and is a fixture of maritime shipping (deep dive) reporting. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Claim Value / Cargo Value Carried; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. In Maritime, it is a recognized element of the standard performance toolkit.

## Formula

```
CDCR-D = Claim Value / Cargo Value Carried
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** maritime_shipping_deep_dive
- **Sector:** maritime

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2439 (batch 6)
