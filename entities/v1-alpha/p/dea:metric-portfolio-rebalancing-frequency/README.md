# dea:metric-portfolio-rebalancing-frequency

Candidate Performance Metric record for **Portfolio Rebalancing Frequency** (PRF-PPM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-portfolio-rebalancing-frequency`
- **Name:** Portfolio Rebalancing Frequency
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PRF-PPM

## 2. Definition

Portfolio Rebalancing Frequency (PRF-PPM) captures conformance to standards, plans, or obligations for organizations tracking program & portfolio management. It is computed as Quarterly Rebalance Decisions Executed / Required, expressed in times per period. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how often investment is genuinely reallocated based on performance and strategy shifts. Periods between rebalances are periods of strategy drift. Rebalancing that shuffles only marginal budgets is churn, not management. Read with initiative kill decision timeliness and strategic alignment score - initiatives.

## Formula

```
PRF-PPM = Quarterly Rebalance Decisions Executed / Required
```

## Unit

- **Unit reference:** `dea:unit-times`
- **Unit:** times
- **Unit label (as published):** times per period

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** program_portfolio_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2967 (batch 7)
