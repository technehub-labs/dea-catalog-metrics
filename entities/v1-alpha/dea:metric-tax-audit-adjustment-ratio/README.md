# dea:metric-tax-audit-adjustment-ratio

Candidate Performance Metric record for **Tax Audit Adjustment Ratio** (TAAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-tax-audit-adjustment-ratio`
- **Name:** Tax Audit Adjustment Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TAAR

## 2. Definition

Tax Audit Adjustment Ratio (TAAR) captures exposure to adverse outcomes for organizations tracking tax & fiscal. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Tax Audit Adjustments / Taxes Originally Declared, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures audit adjustments relative to originally filed positions. It matters because it is the report card on whether tax positions survive scrutiny. Positions can be structured to defer adjustments beyond measurement windows, flattering the ratio. Read with Tax Provision Accuracy and audit cycle history to confirm positions hold across full audit horizons.

## Formula

```
TAAR = Tax Audit Adjustments / Taxes Originally Declared
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** tax_fiscal

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 610 (batch 2)
