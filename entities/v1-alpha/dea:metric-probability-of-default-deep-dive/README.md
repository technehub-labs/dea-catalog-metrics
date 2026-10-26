# dea:metric-probability-of-default-deep-dive

Candidate Performance Metric record for **Probability of Default (Deep Dive)** (PDDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-probability-of-default-deep-dive`
- **Name:** Probability of Default (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PDDD

## 2. Definition

Probability of Default (Deep Dive) (PDDD) addresses exposure to adverse outcomes and is a fixture of credit & collections risk (enterprise) reporting. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Modeled Likelihood of Borrower Default within Horizon; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the likelihood a borrower defaults within a horizon. PD is the first pillar of expected credit loss. PD models calibrated on benign vintages fail in regime turns. Read with expected loss rate (Deep Dive) and vintage default emergence curve.

## Formula

```
PDDD = Modeled Likelihood of Borrower Default within Horizon
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** credit_collections_risk_enterprise

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4195 (batch 9)
