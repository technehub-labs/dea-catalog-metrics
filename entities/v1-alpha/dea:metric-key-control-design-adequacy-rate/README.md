# dea:metric-key-control-design-adequacy-rate

Candidate Performance Metric record for **Key Control Design Adequacy Rate** (KCDAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-key-control-design-adequacy-rate`
- **Name:** Key Control Design Adequacy Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** KCDAR

## 2. Definition

Within Internal Controls & Financial Reporting Integrity, Key Control Design Adequacy Rate (KCDAR) is used to gauge the quality of outputs and outcomes. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Key Controls Assessed as Adequately Designed / Key Controls, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures whether key controls, as designed, would actually mitigate the risks they address. Design adequacy is the first gate: a perfectly operated irrelevant control still fails. Design rated by control owners rather than independent reviewers inflates. Read with key control operating effectiveness rate and internal control design effectiveness.

## Formula

```
KCDAR = Key Controls Assessed as Adequately Designed / Key Controls
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** internal_controls_financial_reporting_integrity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3575 (batch 8)
