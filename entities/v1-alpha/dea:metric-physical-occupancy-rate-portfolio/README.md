# dea:metric-physical-occupancy-rate-portfolio

Candidate Performance Metric record for **Physical Occupancy Rate (Portfolio)** (POR-P) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-physical-occupancy-rate-portfolio`
- **Name:** Physical Occupancy Rate (Portfolio)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** POR-P

## 2. Definition

A Real Estate Portfolio & Property Management indicator, Physical Occupancy Rate (Portfolio) (POR-P) quantifies the utilization or availability of capacity. Its calculation is Occupied Units or Area / Total Units or Area, measured in percent (%). It originates from and is most used in Real Estate practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of leasable space physically occupied. It is the demand signal of a portfolio, but physical occupancy alone can mask under-renting: filled space at distressed rates is weakness, not strength. Lease-expiry walls belong next to occupancy, since stability of the occupied share is what lenders price. Read with economic occupancy rate and tenant retention rate (Portfolio).

## Formula

```
Occupied Units or Area / Total Units or Area
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** real_estate_portfolio_property_management
- **Sector:** real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1740 (batch 6)
