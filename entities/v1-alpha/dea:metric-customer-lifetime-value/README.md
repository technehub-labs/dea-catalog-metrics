# dea:metric-customer-lifetime-value

Candidate Performance Metric record for **Customer Lifetime Value** (CLV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-customer-lifetime-value`
- **Name:** Customer Lifetime Value
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CLV

## 2. Definition

A Customer indicator, Customer Lifetime Value (CLV) quantifies the economic value created or preserved. It is defined as Average Revenue per Customer x Gross Margin x Average Lifespan; the result is stated in currency value. Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

The present value of all margin a customer relationship will generate - the denominator-era metric of relationship economics, credited in its modern form to the direct-marketing literature that first insisted customers be valued as assets rather than transactions. LTV converts retention, margin, and discounting into a single capital-like number that can be compared directly with acquisition cost, turning marketing from expense into investment. Its strategic danger is specious precision: inputs (churn, margin expansion, discount rate) are assumptions wearing decimal places, and LTV models have justified reckless acquisition in every cycle. The defensive discipline is to recompute LTV from realized cohort data each period and let observed behavior override the model that predicted it.

## Formula

```
Average Revenue per Customer x Gross Margin x Average Lifespan
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
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** customer

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 73 (batch 1)
