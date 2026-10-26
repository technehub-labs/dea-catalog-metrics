# dea:metric-average-revenue-per-subscriber

Candidate Performance Metric record for **Average Revenue per Subscriber** (ARPS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-revenue-per-subscriber`
- **Name:** Average Revenue per Subscriber
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ARPS

## 2. Definition

Average Revenue per Subscriber (ARPS) measures the economic value created or preserved in the Media & Entertainment domain. It is computed as Subscription Revenue / Average Subscribers, expressed in currency per unit. Its use is concentrated in Media & entertainment. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Subscription and related revenue per subscriber per month - the monetization metric of subscription media, and the lever that the industry's maturity forced: once subscriber growth saturates, price and packaging become the only growth left, and ARPU is where every pricing action lands. Its strategic significance is the tier-structure read: ARPU movements decompose into plan mix (standard versus premium versus ad-supported), price changes, and discounting - and the ad-tier era complicated the metric by trading ARPU for advertising yield, meaning the honest comparison is now total-revenue-per-subscriber across subscription and ad lines. The measurement honesty is promo-mix awareness: subscriber-counting conventions for bundled, promotional, and free-trial populations differ across services enough to move ARPU materially without any pricing change. Read with churn: price-driven ARPU growth that churns its base is monetization of the future for the present - the trade the metric exists to police.

## Formula

```
Subscription Revenue / Average Subscribers
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** value_delivery
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 694 (batch 2)
