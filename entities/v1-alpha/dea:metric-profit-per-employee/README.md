# dea:metric-profit-per-employee

Candidate Performance Metric record for **Profit per Employee** (PPE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-profit-per-employee`
- **Name:** Profit per Employee
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PPE

## 2. Definition

A Human Resources indicator, Profit per Employee (PPE) quantifies the economic value created or preserved. Its calculation is Operating Profit / Average Headcount, measured in currency value. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Operating or net profit over headcount - the sharpened version of revenue per employee that refuses to be impressed by unprofitable scale. Two companies can post identical revenue per head while one earns a fifth of the profit, and this metric makes that difference visible, which is why productivity-focused investors and value-creation plans prefer it. It captures the compounding of both productivity and margin discipline in one number, and its trend through a transformation program is the single best summary of whether the program worked. The caveat is mix: outsourced work and contractor-heavy models shift labor off the employee count and flatter the number, so read alongside revenue per full-time-equivalent including contractors when the operating model uses them heavily.

## Formula

```
Operating Profit / Average Headcount
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** organization
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** human_resources

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 137 (batch 1)
