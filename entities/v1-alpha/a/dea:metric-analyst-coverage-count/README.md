# dea:metric-analyst-coverage-count

Candidate Performance Metric record for **Analyst Coverage Count** (ANCC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-analyst-coverage-count`
- **Name:** Analyst Coverage Count
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ANCC

## 2. Definition

Analyst Coverage Count (ANCC) captures the economic value created or preserved for organizations tracking investor relations & capital markets. Its calculation is Sell-Side Analysts Publishing Estimates, measured in count (items per period). It originates from and is most used in Listed companies practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The number of sell-side analysts publishing estimates on the stock - the market-attention metric whose significance is the information economics it proxies: coverage means the company is being continuously modeled, and that modeling produces earnings forecasts, price targets, and the comparative context that institutional investors require to act. Coverage matters functionally: below a handful of analysts, a stock lacks the estimate infrastructure that indexes, screens, and mandates are built on, and the company becomes hard to buy in size - which is why IR programs treat coverage initiation as an objective. The honest read is quality-weighted: coverage from analysts with strong track records and sector depth moves prices more than headline count, and coverage that merely repeats guidance adds attention without adding information. Read with the estimate dispersion, since a covered stock with wildly divergent estimates is getting attention without achieving consensus - a different problem than no coverage.

## Formula

```
ANCC = Sell-Side Analysts Publishing Estimates
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investor_relations_capital_markets
- **Sector:** listed_companies

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 623 (batch 2)
