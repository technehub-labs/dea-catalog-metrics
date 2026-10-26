# dea:metric-cost-recovery-per-performance

Candidate Performance Metric record for **Cost Recovery per Performance** (CRPP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-recovery-per-performance`
- **Name:** Cost Recovery per Performance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CRPP

## 2. Definition

Within Arts & Culture, Cost Recovery per Performance (CRPP) is used to gauge the economic value created or preserved. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Earned Revenue / Direct Production Costs, measured in ratio (x:1 or x). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Arts & culture practice.

## 3. Context

Cost recovery per performance measures earned revenue against the cost of mounting each performance, and it is the unit-economics metric of performing arts - the sector's structural reality is that ticket revenue rarely covers production cost (the so-called income gap, historically funded by donors and subsidies), so cost recovery per performance measures how much of the gap each performance fills. The metric decomposes into capacity utilization (filled seats against house) and price realization (average yield versus potential), and the production-cost structure (scale of staging, orchestra size, venue cost) sets the denominator. Read with capacity utilization and yield separately, genre-mix recovery differences (a mainstage opera and a studio recital recover at wildly different rates), and donor-subsidy attribution since some programming exists for mission rather than recovery.

## Formula

```
CRPP = Earned Revenue / Direct Production Costs
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** arts_culture
- **Sector:** arts_culture

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1223 (batch 4)
