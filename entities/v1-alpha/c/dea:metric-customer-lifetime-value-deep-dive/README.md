# dea:metric-customer-lifetime-value-deep-dive

Candidate Performance Metric record for **Customer Lifetime Value (Deep Dive)** (LTVDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-customer-lifetime-value-deep-dive`
- **Name:** Customer Lifetime Value (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** LTVDD

## 2. Definition

Customer Lifetime Value (Deep Dive) (LTVDD) measures the economic value created or preserved in the Unit Economics & Growth (Deep Dive) domain. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Average Gross Margin per Customer x Lifespan, measured in currency value. Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Software practice.

## 3. Context

Measures the total predicted value of a customer relationship. LTV is the numerator of growth economics and the ceiling on rational CAC. LTV models built on optimistic retention assumptions are hope compounded. Read with LTV to CAC ratio and cohort retention curve stability.

## Formula

```
LTVDD = Average Gross Margin per Customer x Lifespan
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** unit_economics_growth_deep_dive
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4156 (batch 9)
