# dea:metric-credit-score-population-drift

Candidate Performance Metric record for **Credit Score Population Drift** (CSPD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-credit-score-population-drift`
- **Name:** Credit Score Population Drift
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CSPD

## 2. Definition

Within Credit & Collections Risk (Enterprise), Credit Score Population Drift (CSPD) is used to gauge exposure to adverse outcomes. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Period Shift in Score Distribution of Book vs Origination - reported in index (0-100 or normalized). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Period Shift in Score Distribution of Book vs Origination
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** credit_collections_risk_enterprise

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4205 (batch 9)
