# dea:metric-break-even-load-factor

Candidate Performance Metric record for **Break-even Load Factor** (BELF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-break-even-load-factor`
- **Name:** Break-even Load Factor
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BELF

## 2. Definition

Break-even Load Factor (BELF) captures exposure to adverse outcomes for organizations tracking airline operations (deep dive). Its calculation is Load Factor Required to Cover Costs, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. It originates from and is most used in Airlines practice.

## 3. Context

Measures the occupancy required to cover operating costs at current yields and unit costs. It is the fragility gauge of the business model: the gap between breakeven and actual load factor is the buffer against demand shocks, and network decisions (new routes, aircraft changes) are stress-tested against it. Breakevens computed on favorable fuel or currency assumptions understate true fragility. Read with load factor (Deep Dive) and unit revenue and cost trends.

## Formula

```
BELF = Load Factor Required to Cover Costs
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airline_operations_deep_dive
- **Sector:** airlines

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2255 (batch 6)
