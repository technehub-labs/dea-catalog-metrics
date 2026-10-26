# dea:metric-subscriber-growth-rate

Candidate Performance Metric record for **Subscriber Growth Rate** (SBGR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-subscriber-growth-rate`
- **Name:** Subscriber Growth Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SBGR

## 2. Definition

Subscriber Growth Rate (SBGR) captures growth over time for organizations tracking media & entertainment. Its calculation is (Subscribers_current - Subscribers_prior) / Subscribers_prior, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Media & entertainment practice.

## 3. Context

Period growth in paying subscribers - the headline metric of the streaming era, and the one entire content and distribution strategies are built on: subscriptions are the recurring-revenue base, and its growth is what the model's valuation rests on. Its strategic significance is the volume-versus-price structure: streaming businesses have historically competed on subscriber growth at the expense of near-term profit, on the logic that scale in subscriptions funds the content flywheel, and the growth rate is the pace gauge of that strategy - which is why subscriber announcements move streamer valuations more than earnings do. The honest read is net and quality-adjusted: growth gross of churn is a treadmill metric, growth driven by promotional pricing reverts at renewal, and paid-sharing and ad-tier experiments change what a subscriber even is. Read with ARPU and churn companions, since growth that dilutes per-subscriber economics is the classic scaling trap the headline rate never shows.

## Formula

```
(Subscribers_current - Subscribers_prior) / Subscribers_prior
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** media_entertainment
- **Sector:** media_entertainment

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 692 (batch 2)
