# dea:metric-customer-acquisition-cost

Candidate Performance Metric record for **Customer Acquisition Cost** (CAC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-customer-acquisition-cost`
- **Name:** Customer Acquisition Cost
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CAC

## 2. Definition

A Banking & Financial Services indicator, Customer Acquisition Cost (CAC) quantifies how efficiently resources are converted into outputs. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Total Sales and Marketing Cost / New Customers Acquired, expressed in currency per unit. It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Financial services.

## 3. Context

The fully loaded cost of sales and marketing divided by new customers acquired - the entry ticket of unit economics and the number every growth investor asks for first. Its strategic content is entirely in the comparison with customer lifetime value: LTV to CAC near or below 1 means the company pays for customers who never pay it back, while very high multiples invite competition to arbitrage the same channel. The definitional games are endless - blended CAC mixes organic with paid, period costs can be expensed against later cohorts - so paid CAC by cohort and channel is the honest cut. Watch the denominator effect: as the addressable market saturates, CAC inflates structurally, and the metric itself is the earliest warning of saturation.

## Formula

```
Total Sales and Marketing Cost / New Customers Acquired
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** banking_financial_services
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 54 (batch 1)
