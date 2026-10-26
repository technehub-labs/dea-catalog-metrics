# dea:metric-program-interdependency-health

Candidate Performance Metric record for **Program Interdependency Health** (PIH-PPM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-program-interdependency-health`
- **Name:** Program Interdependency Health
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PIH-PPM

## 2. Definition

Program Interdependency Health (PIH-PPM) captures exposure to adverse outcomes for organizations tracking program & portfolio management. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Cross-Program Milestones on Track / Cross-Program Milestones, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the status quality of commitments between programs and initiatives. Interdependencies are the joints where portfolios break. Health scoring without named owners and dates is decoration. Read with portfolio dependency visibility coverage and dependency closure timeliness.

## Formula

```
PIH-PPM = Cross-Program Milestones on Track / Cross-Program Milestones
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
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** program_portfolio_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2962 (batch 7)
