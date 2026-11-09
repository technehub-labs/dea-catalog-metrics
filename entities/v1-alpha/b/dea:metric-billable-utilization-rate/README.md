# dea:metric-billable-utilization-rate

Candidate Performance Metric record for **Billable Utilization Rate** (BUR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-billable-utilization-rate`
- **Name:** Billable Utilization Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BUR

## 2. Definition

Billable Utilization Rate (BUR) measures the utilization or availability of capacity in the Professional Services domain. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Billable Hours / Available Hours, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Professional services practice.

## 3. Context

Billable hours as a share of available working hours - the revenue-productivity metric of professional services, and the one that sits closest to the profit engine: salary cost is fixed per person, so each additional billable point falls almost entirely to gross margin, and utilization is the multiplier that turns headcount cost into revenue. Its strategic significance is the capacity it reveals: firms chronically misjudge how much of their people's time is billable, and the gap between assumed and actual utilization is where profit forecasts go wrong. The definitional honesty is the denominator: total employed hours versus standard client-billing hours versus hours-excluding-training-and-bench differ materially, and utilization quoted without its denominator convention is nearly meaningless. Read with the leverage of the pyramid: senior staff billing high means a pricing problem, junior staff billing low means a training or staffing problem, and the utilization-by-level view is where the diagnosis lives.

## Formula

```
BUR = Billable Hours / Available Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** professional_services
- **Sector:** professional_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 678 (batch 2)
