# dea:metric-benefit-cost-per-employee

Candidate Performance Metric record for **Benefit Cost per Employee** (BCPE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-benefit-cost-per-employee`
- **Name:** Benefit Cost per Employee
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BCPE

## 2. Definition

Benefit Cost per Employee (BCPE) captures the economic value created or preserved for organizations tracking standard workforce & pay metrics. The formula is Total Benefits Spend / Employees - reported in currency per unit. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures total benefits spend per head. Benefits are a large and rising share of total employment cost. Cost per head without participation and outcome data is half the picture. Read with benefits utilization rate and total compensation cost per employee.

## Formula

```
BCPE = Total Benefits Spend / Employees
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** organization
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** standard_workforce_pay_metrics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4129 (batch 9)
