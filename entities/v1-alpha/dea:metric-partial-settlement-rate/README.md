# dea:metric-partial-settlement-rate

Candidate Performance Metric record for **Partial Settlement Rate** (PSR-C) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-partial-settlement-rate`
- **Name:** Partial Settlement Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PSR-C

## 2. Definition

Partial Settlement Rate (PSR-C) addresses exposure to adverse outcomes and is a fixture of insurance claims deep dive reporting. It is a working-level control: thresholds trigger immediate operational response. It is defined as Claims Partially Settled then Closed / Claims; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. In Insurance, it is a recognized element of the standard performance toolkit.

## Formula

```
Claims Partially Settled then Closed / Claims
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_claims_deep_dive
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1555 (batch 6)
