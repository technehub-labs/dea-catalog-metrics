# dea:metric-guest-satisfaction-post-visit-survey-deep-dive

Candidate Performance Metric record for **Guest Satisfaction - Post-Visit Survey (Deep Dive)** (GSPS-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-guest-satisfaction-post-visit-survey-deep-dive`
- **Name:** Guest Satisfaction - Post-Visit Survey (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** GSPS-D

## 2. Definition

Guest Satisfaction - Post-Visit Survey (Deep Dive) (GSPS-D) measures the engagement or satisfaction of the people involved in the Restaurant Operations (Deep Dive) domain. It is computed as Average Post-Visit Rating, expressed in score (points). Its use is concentrated in Restaurants. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures guest sentiment captured after the dining experience. In a review-driven industry, satisfaction is the demand engine: ratings gate discovery platforms, and repeat visitation follows scores with reliable lag. Response bias is the measurement trap - very satisfied and very upset guests respond, the middle does not - so triangulate with review-site sentiment. Read with online review scores and complaint resolution patterns.

## Formula

```
GSPS-D = Average Post-Visit Rating
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** engagement
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** restaurant_operations_deep_dive
- **Sector:** restaurants

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2357 (batch 6)
