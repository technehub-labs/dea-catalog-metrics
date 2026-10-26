# dea:metric-portfolio-vacancy-rate

Candidate Performance Metric record for **Portfolio Vacancy Rate** (PVR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-portfolio-vacancy-rate`
- **Name:** Portfolio Vacancy Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PVR

## 2. Definition

Portfolio Vacancy Rate (PVR) measures the utilization or availability of capacity in the Facilities & Real Estate domain. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Vacant Leasable Area / Total Leasable Area, measured in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The share of portfolio space or units vacant and unleased - the asset-performance metric of the landlord side, and the number that dominates asset valuation since income capitalization treats vacancy as permanent revenue loss. Its strategic significance is the cycle gauge: vacancy leads rent (vacant space gets discounted first), so the vacancy rate is the leading indicator of the rental cycle, and the balance between vacant space and net absorption is what tells a landlord whether weakness is oversupply (wait) or demand decline (act). The honest measurement separates physical from economic vacancy: space leased but at reduced rent or with heavy incentives is physically occupied and economically half-empty, which is why rent-incentive data must be read alongside the vacancy trend. By segment matters: headline vacancy can be fine while an entire floor-plate class or market sits empty.

## Formula

```
Vacant Leasable Area / Total Leasable Area
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** facilities_real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 455 (batch 1)
