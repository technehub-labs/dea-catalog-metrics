# dea:metric-regulatory-penalty-exposure-ratio

Candidate Performance Metric record for **Regulatory Penalty Exposure Ratio** (RPER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-regulatory-penalty-exposure-ratio`
- **Name:** Regulatory Penalty Exposure Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RPER

## 2. Definition

Regulatory Penalty Exposure Ratio (RPER) measures exposure to adverse outcomes in the Legal Operations domain. Its calculation is Aggregate Penalty Exposure / Revenue, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures potential or realized penalty exposure against legal or compliance budgets. It converts diffuse regulatory risk into an expected-cost number suitable for board reporting. Estimates of exposure depend heavily on enforcement climate modeling, which drifts quickly, so date-stamp assumptions and refresh. Read with regulatory fines and penalties ratio (realized) and compliance risk assessment coverage.

## Formula

```
RPER = Aggregate Penalty Exposure / Revenue
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** legal_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1679 (batch 6)
