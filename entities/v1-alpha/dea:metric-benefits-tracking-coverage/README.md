# dea:metric-benefits-tracking-coverage

Candidate Performance Metric record for **Benefits Tracking Coverage** (BTC-PPM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-benefits-tracking-coverage`
- **Name:** Benefits Tracking Coverage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** BTC-PPM

## 2. Definition

Benefits Tracking Coverage (BTC-PPM) captures conformance to standards, plans, or obligations for organizations tracking program & portfolio management. Its calculation is Initiatives with Measurable Benefits Tracked / Initiatives, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of initiatives with defined, owned, measurable benefits under active tracking. Tracking is the difference between a benefits-led portfolio and a spend-led one. Coverage with unmeasurable benefit statements (better customer experience) is nominal. Read with benefits realization rate and portfolio value delivery rate.

## Formula

```
Initiatives with Measurable Benefits Tracked / Initiatives
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2963 (batch 7)
