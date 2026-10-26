# dea:metric-sales-ramp-time

Candidate Performance Metric record for **Sales Ramp Time** (SRT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-sales-ramp-time`
- **Name:** Sales Ramp Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SRT

## 2. Definition

Sales Ramp Time (SRT) measures the utilization or availability of capacity in the Sales domain. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Months from Hire to Full Quota Attainment - reported in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how long a new rep takes to reach full productivity. It matters because it determines hiring lead time and the true cost of turnover in sales. Definitions vary on the productivity threshold, so teams can quietly lower the bar to show faster ramps. Read with New Hire 90-Day Retention and Quota Attainment to check that fast ramps produce sustained performance, not early lucky deals.

## Formula

```
Months from Hire to Full Quota Attainment
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** customer
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sales

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 100 (batch 1)
