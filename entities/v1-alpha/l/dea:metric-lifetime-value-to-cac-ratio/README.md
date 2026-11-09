# dea:metric-lifetime-value-to-cac-ratio

Candidate Performance Metric record for **Lifetime Value to CAC Ratio** (LTV:CAC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-lifetime-value-to-cac-ratio`
- **Name:** Lifetime Value to CAC Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** LTV:CAC

## 2. Definition

Lifetime Value to CAC Ratio (LTV:CAC) measures the economic value created or preserved in the Banking & Financial Services domain. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Customer Lifetime Value / Customer Acquisition Cost, measured in ratio (x:1 or x). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Financial services practice.

## 3. Context

Customer lifetime value divided by acquisition cost - the single number that adjudicates whether a growth engine is a machine or a bonfire. A ratio of three is the folk convention for healthy; below one, the company destroys value with every sale; far above five suggests underinvestment in growth, leaving channels open for competitors. The metric's honesty depends entirely on the LTV construction: lifetime value computed from churn projections can be whatever the model wants, so disciplined operators ground it in observed cohort behavior with gross margin and payback included. The pairing metric is payback period - a ratio of four with a 30-month payback can drown a company before the value arrives.

## Formula

```
LTV:CAC = Customer Lifetime Value / Customer Acquisition Cost
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** banking_financial_services
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 55 (batch 1)
