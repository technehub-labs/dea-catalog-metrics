# dea:metric-guest-satisfaction-index

Candidate Performance Metric record for **Guest Satisfaction Index** (GSI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-guest-satisfaction-index`
- **Name:** Guest Satisfaction Index
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** GSI

## 2. Definition

A Hospitality & Food Service indicator, Guest Satisfaction Index (GSI) quantifies the engagement or satisfaction of the people involved. It is computed as Weighted Guest Survey Score, expressed in index (0-100 or normalized). Its use is concentrated in Hospitality. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The composite of guest-reported experience across stay dimensions - cleanliness, service, quality, value - conventionally through standardized post-stay survey instruments, and in the review era, increasingly correlated with the public review scores that no survey can outrank. Its strategic significance is the demand-side economics it predicts: satisfaction drives review scores, review scores drive booking conversion on the platforms that intermediate demand, and the satisfaction-to-revenue chain is now visible and priced. The honest read is dimension-level: overall indices hide that cleanliness and service-recovery items move loyalty more than amenity items, which is where investment should go. Read with the response-rate caveat: satisfied guests respond more, so unadjusted indices run optimistic, and the trend matters more than the level.

## Formula

```
Weighted Guest Survey Score
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** customer
- **Purpose classification:** engagement
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** hospitality_food_service
- **Sector:** hospitality

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 511 (batch 1)
