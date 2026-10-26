# dea:metric-perfect-order-rate

Candidate Performance Metric record for **Perfect Order Rate** (POR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-perfect-order-rate`
- **Name:** Perfect Order Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** POR

## 2. Definition

Perfect Order Rate (POR) addresses the quality of outputs and outcomes and is a fixture of operations reporting. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Orders Delivered Complete, On Time, Damage-Free, Correctly Documented / Total Orders, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The share of orders delivered complete, on time, damage-free, and with accurate documentation - all four conditions jointly, which is what makes it the gold standard of customer-facing logistics measurement. Because it multiplies component probabilities, the arithmetic punishes mediocrity: an operation at 95 percent on each of the four elements delivers a perfect order only 81 percent of the time, and lifting the composite to 98 forces every element above 99.5. That multiplicative structure is its strategic value - it refuses to let component metrics hide each other - and it maps directly to the cost of failure, since each imperfect order generates expediting, credits, and call-center contact with quantifiable cost. Benchmarks vary wildly by industry, so trend and cost-per-failure beat absolute comparisons.

## Formula

```
Orders Delivered Complete, On Time, Damage-Free, Correctly Documented / Total Orders
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 160 (batch 1)
