# dea:metric-monthly-churn-streaming

Candidate Performance Metric record for **Monthly Churn (Streaming)** (MCH) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-monthly-churn-streaming`
- **Name:** Monthly Churn (Streaming)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MCH

## 2. Definition

A Media & Entertainment indicator, Monthly Churn (Streaming) (MCH) quantifies exposure to adverse outcomes. It is defined as Cancelled Subscriptions / Subscribers at Start of Month; the result is stated in percent (%). In Media & entertainment, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Subscribers lost per month - the retention metric of subscription media, whose strategic significance is the content-economics coupling: subscriber lifetimes must be long enough to amortize the content spend that attracted them, and monthly churn in the low single digits is the arithmetic dividing the services that compound from those that tread water. The read that matters is reason- and cohort-coded: churn driven by content-exhaustion (binged the show they came for, then left) is a content-strategy signal, churn driven by price is a packaging signal, and the returning-subscriber pattern (churn and rejoin around tentpole releases) is a behavior specific to this industry that simple churn math punishes incorrectly. Read with the engagement-depth dimension: subscribers near-zero viewing churn predictably months out, which is why streaming services maintain internal engagement-health scores - churn's leading indicator - and why headline churn is always a lagging number in this business.

## Formula

```
Cancelled Subscriptions / Subscribers at Start of Month
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** media_entertainment
- **Sector:** media_entertainment

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 693 (batch 2)
