# dea:metric-online-order-mix

Candidate Performance Metric record for **Online Order Mix** (OOM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-online-order-mix`
- **Name:** Online Order Mix
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** OOM

## 2. Definition

Online Order Mix (OOM) captures growth over time for organizations tracking restaurants. Its calculation is Digital Orders / Total Orders, measured in percent (%). It originates from and is most used in Restaurants practice. Its value drives prioritization and resource reallocation among competing initiatives. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of orders arriving through digital channels. It matters because digital orders scale capacity and carry richer data, but third-party fees erode margin. Ordering direct can be pushed at the cost of guest convenience. Read with Channel Profitability per Order and Guest Satisfaction to confirm mix strategy is economically sound.

## Formula

```
Digital Orders / Total Orders
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
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** restaurants
- **Sector:** restaurants

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 944 (batch 3)
