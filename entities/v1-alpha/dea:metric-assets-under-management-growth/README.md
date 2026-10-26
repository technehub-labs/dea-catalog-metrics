# dea:metric-assets-under-management-growth

Candidate Performance Metric record for **Assets Under Management Growth** (AUMG) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-assets-under-management-growth`
- **Name:** Assets Under Management Growth
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** AUMG

## 2. Definition

Assets Under Management Growth (AUMG) captures growth over time for organizations tracking banking & financial services. The formula is (AUM_current - AUM_prior) / AUM_prior - reported in percent (%). It is a standard measure in the Financial services sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Period growth in total client assets managed - the top-line expansion metric for asset managers, where the revenue model (a fee on assets) makes AUM the denominator of everything. Growth decomposes into three mechanically distinct drivers: market appreciation (free but volatile), net inflows (the genuine franchise signal), and acquisitions. A manager can post double-digit AUM growth in a bull market while bleeding clients - which is why net flows, not headline growth, is the metric professional evaluators track. Strategic use is capacity and pricing power: sustained inflows into strategies with fee pressure reveal the difference between a distribution machine and a performance-driven franchise.

## Formula

```
(AUM_current - AUM_prior) / AUM_prior
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** growth
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 53 (batch 1)
