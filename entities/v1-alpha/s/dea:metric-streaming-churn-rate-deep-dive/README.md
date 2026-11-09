# dea:metric-streaming-churn-rate-deep-dive

Candidate Performance Metric record for **Streaming Churn Rate (Deep Dive)** (SCR-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-streaming-churn-rate-deep-dive`
- **Name:** Streaming Churn Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SCR-S

## 2. Definition

Within Broadcasting & Streaming Media, Streaming Churn Rate (Deep Dive) (SCR-S) is used to gauge the retention of customers, users, or assets over time. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Cancelled Subscriptions / Subscribers - reported in percent (%). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Media & Entertainment sector.

## 3. Context

Measures subscriber cancellation, often monthly in a churn-intensive subscription business. It is the sustainability metric of streaming economics: content spend is fixed-cost, so subscriber lifetime determines whether the model works at all. Churn driven by binge-and-cancel behavior is structural, not a service failure, so segment by content anniversaries and bundle composition. Read with monthly viewing hours per subscriber and acquisition-versus-returning churn splits.

## Formula

```
SCR-S = Cancelled Subscriptions / Subscribers
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** retention
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** broadcasting_streaming_media
- **Sector:** media_entertainment

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1956 (batch 6)
