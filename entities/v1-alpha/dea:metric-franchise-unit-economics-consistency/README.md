# dea:metric-franchise-unit-economics-consistency

Candidate Performance Metric record for **Franchise Unit Economics Consistency** (FUEC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-franchise-unit-economics-consistency`
- **Name:** Franchise Unit Economics Consistency
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FUEC

## 2. Definition

Franchise Unit Economics Consistency (FUEC) captures exposure to adverse outcomes for organizations tracking franchise operations (deep dive). Its calculation is Units within EBITDA Band / Total Units, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the dispersion of franchisee profitability across the system. It is the health metric beneath system growth: a franchise model only works when the median operator makes money, and widening dispersion signals that the model fits fewer and fewer locations or operators. Consistency measured only among surviving franchisees ignores survivorship bias, which is the standard illusion. Read with franchisee churn and new franchise ramp time (Deep Dive).

## Formula

```
Units within EBITDA Band / Total Units
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** franchise_operations_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2218 (batch 6)
