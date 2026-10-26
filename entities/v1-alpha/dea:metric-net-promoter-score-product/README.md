# dea:metric-net-promoter-score-product

Candidate Performance Metric record for **Net Promoter Score (Product)** (NPS-P) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-net-promoter-score-product`
- **Name:** Net Promoter Score (Product)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** NPS-P

## 2. Definition

A Product Management indicator, Net Promoter Score (Product) (NPS-P) quantifies the engagement or satisfaction of the people involved. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is % Promoters - % Detractors among Product Users, measured in score (points). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The recommend-intent metric applied to the product experience - promoters minus detractors on the 0-10 recommend scale, with the product-function cut that separates what the product itself earns from what the brand or service earns. Its strategic significance is attribution honesty: enterprise NPS blends product, support, price, and relationship, and the product-specific cut is what product teams can actually act on, since it correlates with usage depth and feature satisfaction rather than with account management. The methodological inheritance includes the same caveats as the parent metric - the scale's threshold conventions, the response bias, and the cultural variation of recommendation enthusiasm across markets. Read with behavioral companions: stickiness, retention, and feature-level satisfaction scores, because recommend-intent is a claim and retention is the evidence.

## Formula

```
% Promoters - % Detractors among Product Users
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
- **Domain:** product_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 553 (batch 1)
