# dea:metric-combined-ratio

Candidate Performance Metric record for **Combined Ratio** (CoR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-combined-ratio`
- **Name:** Combined Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CoR

## 2. Definition

A Insurance indicator, Combined Ratio (CoR) quantifies the economic value created or preserved. It is defined as (Incurred Losses + Expenses) / Earned Premiums; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Lower values are better; each reduction is an improvement. In Insurance, it is a recognized element of the standard performance toolkit.

## 3. Context

The combined ratio - loss ratio plus expense ratio - is the insurance industry's headline profitability gauge: below 100% an insurer earns an underwriting profit; above 100% it pays out more than it earns in premium and relies on investment income. A 98% combined ratio means 2 cents of underwriting profit per premium dollar. It is highly cyclical (hard and soft markets swing it by double digits), so compare across years and reserve development, not just one period - and note that reserve changes retroactively restate it.

## Formula

```
(Incurred Losses + Expenses) / Earned Premiums
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** insurance
- **Sector:** insurance

## Attribution

- **Source credit:** Insurance statutory reporting practice

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 58 (batch 1)
