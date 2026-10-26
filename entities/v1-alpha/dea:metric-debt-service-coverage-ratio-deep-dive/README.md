# dea:metric-debt-service-coverage-ratio-deep-dive

Candidate Performance Metric record for **Debt Service Coverage Ratio (Deep Dive)** (DSCRDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-debt-service-coverage-ratio-deep-dive`
- **Name:** Debt Service Coverage Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DSCRDD

## 2. Definition

Debt Service Coverage Ratio (Deep Dive) (DSCRDD) captures exposure to adverse outcomes for organizations tracking valuation & corporate finance standard measures. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Operating Income / Total Debt Service; the result is stated in ratio (x:1 or x). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures cash available to service principal plus interest. DSCR is the covenant-level solvency test lenders actually enforce. Ratios computed on EBITDA rather than cash overstate reliability. Read with interest coverage ratio (Statement Analysis) and liquidity coverage ratio (Fund Ops).

## Formula

```
Operating Income / Total Debt Service
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** valuation_corporate_finance_standard_measures

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4050 (batch 9)
