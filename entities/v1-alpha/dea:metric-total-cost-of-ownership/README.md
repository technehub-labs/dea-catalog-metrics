# dea:metric-total-cost-of-ownership

Candidate Performance Metric record for **Total Cost of Ownership** (TCO) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-total-cost-of-ownership`
- **Name:** Total Cost of Ownership
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TCO

## 2. Definition

A Finance & Accounting indicator, Total Cost of Ownership (TCO) quantifies the economic value created or preserved. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Purchase Price + Operating Costs + Maintenance Costs - Residual Value, measured in currency value. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the full lifecycle cost of an asset including purchase, operation, maintenance, and disposal. It matters because cheap acquisition prices often hide far larger operating costs over time. Estimates can be gamed by understating maintenance or downtime assumptions to justify a favored vendor. Read with Maintenance Cost per Asset and Fixed Asset Turnover to test whether lifecycle assumptions held after purchase.

## Formula

```
Purchase Price + Operating Costs + Maintenance Costs - Residual Value
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** finance_accounting

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 32 (batch 1)
