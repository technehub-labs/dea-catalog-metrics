# dea:metric-portfolio-cost-overrun-ratio

Candidate Performance Metric record for **Portfolio Cost Overrun Ratio** (PCOR-PPM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-portfolio-cost-overrun-ratio`
- **Name:** Portfolio Cost Overrun Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PCOR-PPM

## 2. Definition

Within Program & Portfolio Management, Portfolio Cost Overrun Ratio (PCOR-PPM) is used to gauge exposure to adverse outcomes. The formula is Portfolio Overruns / Portfolio Budget - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures aggregate portfolio cost overrun relative to approved budgets. It aggregates project-level variance into the board-level number. A healthy ratio with high variance across projects can hide offsetting lucky and unlucky bets. Read with cost variance percent and portfolio value delivery rate.

## Formula

```
Portfolio Overruns / Portfolio Budget
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** program_portfolio_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2974 (batch 7)
