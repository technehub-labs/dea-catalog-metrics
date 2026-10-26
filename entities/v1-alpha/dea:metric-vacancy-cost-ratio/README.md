# dea:metric-vacancy-cost-ratio

Candidate Performance Metric record for **Vacancy Cost Ratio** (VCR-E) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-vacancy-cost-ratio`
- **Name:** Vacancy Cost Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** VCR-E

## 2. Definition

Within Real Estate Portfolio & Property Management, Vacancy Cost Ratio (VCR-E) is used to gauge exposure to adverse outcomes. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Lost Rent from Vacancy / Gross Potential Rent, measured in percent (%). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Real Estate practice.

## 3. Context

Measures the cost of vacancy - lost rent, operating costs on empty space, incentives - against total revenue. It converts the vacancy line into an actionable P&L item, which focuses management on downtime duration rather than occupancy percentage alone. Distinguish structural vacancy (obsolete space) from frictional vacancy (normal churn), since they need different responses. Read with tenant retention rate (Portfolio) and re-leasing cycle time.

## Formula

```
VCR-E = Lost Rent from Vacancy / Gross Potential Rent
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** real_estate_portfolio_property_management
- **Sector:** real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1749 (batch 6)
