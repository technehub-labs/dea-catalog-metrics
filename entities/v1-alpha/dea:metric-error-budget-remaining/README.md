# dea:metric-error-budget-remaining

Candidate Performance Metric record for **Error Budget Remaining** (EBREM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-error-budget-remaining`
- **Name:** Error Budget Remaining
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** EBREM

## 2. Definition

Error Budget Remaining (EBREM) measures exposure to adverse outcomes in the SRE & Observability Standard Measures domain. The formula is Allowed Errors minus Consumed Errors / Allowed Errors - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Software sector.

## 3. Context

Measures the unused reliability allowance for the current window. Remaining budget is the live license to ship features. Budgets spent unevenly across windows signal systemic reliability problems. Read with error budget consumption rate and error budget policy compliance.

## Formula

```
Allowed Errors minus Consumed Errors / Allowed Errors
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sre_observability_standard_measures
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4375 (batch 11)
