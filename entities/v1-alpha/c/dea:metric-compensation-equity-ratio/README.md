# dea:metric-compensation-equity-ratio

Candidate Performance Metric record for **Compensation Equity Ratio** (CER-PAY) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-compensation-equity-ratio`
- **Name:** Compensation Equity Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CER-PAY

## 2. Definition

Compensation Equity Ratio (CER-PAY) measures conformance to standards, plans, or obligations in the Standard Workforce & Pay Metrics domain. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Top Quartile Pay / Bottom Quartile Pay within Grade, expressed in ratio (x:1 or x). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
CER-PAY = Top Quartile Pay / Bottom Quartile Pay within Grade
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** organization
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** standard_workforce_pay_metrics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4127 (batch 9)
