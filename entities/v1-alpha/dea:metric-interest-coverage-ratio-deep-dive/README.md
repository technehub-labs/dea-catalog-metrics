# dea:metric-interest-coverage-ratio-deep-dive

Candidate Performance Metric record for **Interest Coverage Ratio (Deep Dive)** (ICR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-interest-coverage-ratio-deep-dive`
- **Name:** Interest Coverage Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ICR-D

## 2. Definition

Interest Coverage Ratio (Deep Dive) (ICR-D) addresses exposure to adverse outcomes and is a fixture of balanced scorecard - financial perspective reporting. It is computed as EBIT / Interest Expense, expressed in ratio (x:1 or x). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures earnings available to service interest obligations. Coverage is the canary of solvency: it deteriorates long before default becomes visible. Coverage computed on peak-cycle earnings overstates resilience at the wrong moment. Read with debt to equity and cash flow return on investment.

## Formula

```
EBIT / Interest Expense
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** balanced_scorecard_financial_perspective

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3062 (batch 7)
