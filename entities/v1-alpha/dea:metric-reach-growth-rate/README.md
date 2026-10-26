# dea:metric-reach-growth-rate

Candidate Performance Metric record for **Reach Growth Rate** (RGR-M) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-reach-growth-rate`
- **Name:** Reach Growth Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RGR-M

## 2. Definition

Reach Growth Rate (RGR-M) measures growth over time in the Marketing domain. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as (Reach_current - Reach_prior) / Reach_prior; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures growth in audience reach across channels over time. It matters as a leading indicator of brand momentum before revenue effects show. Vanity reach can be bought through broad low-quality distribution or bot-inflated impressions. Read with Engagement Rate and Marketing Campaign ROI to confirm growing reach is engaged and monetizable.

## Formula

```
(Reach_current - Reach_prior) / Reach_prior
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** marketing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 122 (batch 1)
