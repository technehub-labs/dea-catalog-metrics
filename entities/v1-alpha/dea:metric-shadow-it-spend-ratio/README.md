# dea:metric-shadow-it-spend-ratio

Candidate Performance Metric record for **Shadow IT Spend Ratio** (SITSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-shadow-it-spend-ratio`
- **Name:** Shadow IT Spend Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SITSR

## 2. Definition

Shadow IT Spend Ratio (SITSR) addresses exposure to adverse outcomes and is a fixture of it financial management & technology budgeting reporting. It is defined as Unsanctioned Technology Spend / Total Technology Spend; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures business-unit technology spend occurring outside IT governance. Shadow spend duplicates platforms and creates unmanaged risk. Detection is inherently incomplete, so the ratio is a floor, not a level. Read with showback or chargeback coverage and cybersecurity policy exception rate.

## Formula

```
Unsanctioned Technology Spend / Total Technology Spend
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** it_financial_management_technology_budgeting

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3178 (batch 7)
