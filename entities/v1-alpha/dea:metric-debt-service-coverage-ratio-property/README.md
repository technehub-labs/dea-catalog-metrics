# dea:metric-debt-service-coverage-ratio-property

Candidate Performance Metric record for **Debt Service Coverage Ratio (Property)** (DSCR-P) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-debt-service-coverage-ratio-property`
- **Name:** Debt Service Coverage Ratio (Property)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DSCR-P

## 2. Definition

A Real Estate Portfolio & Property Management indicator, Debt Service Coverage Ratio (Property) (DSCR-P) quantifies exposure to adverse outcomes. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Net Operating Income / Debt Service, measured in ratio (x:1 or x). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Real Estate practice.

## 3. Context

Measures net operating income against debt service at the asset level. It is the solvency floor of leveraged real estate: coverage below the loan covenant threshold converts market weakness into lender control. Stress-read the ratio with realistic vacancy and rate scenarios, since point-in-time coverage hides refinance risk at maturity. Read with weighted debt maturity and loan-to-value evolution.

## Formula

```
Net Operating Income / Debt Service
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** real_estate_portfolio_property_management
- **Sector:** real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1756 (batch 6)
