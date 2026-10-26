# dea:metric-tenant-retention-rate-portfolio

Candidate Performance Metric record for **Tenant Retention Rate (Portfolio)** (TRR-P) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-tenant-retention-rate-portfolio`
- **Name:** Tenant Retention Rate (Portfolio)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** TRR-P

## 2. Definition

Tenant Retention Rate (Portfolio) (TRR-P) addresses the retention of customers, users, or assets over time and is a fixture of real estate portfolio & property management reporting. Its calculation is Leases Renewed / Leases Expiring, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Real Estate practice.

## 3. Context

Measures the share of expiring leases renewed. Retention is the cheapest leasing there is: renewal avoids downtime, fit-out, commissions, and the vacancy drag that compounds. Watch retention bought through deep concessions, which transfers cost from the P&L to the rent roll. Read with net effective rent per square metre and tenant satisfaction score (Portfolio).

## Formula

```
Leases Renewed / Leases Expiring
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** retention
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1743 (batch 6)
