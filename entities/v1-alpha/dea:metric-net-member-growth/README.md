# dea:metric-net-member-growth

Candidate Performance Metric record for **Net Member Growth** (NMG) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-net-member-growth`
- **Name:** Net Member Growth
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** NMG

## 2. Definition

A Fitness & Wellness indicator, Net Member Growth (NMG) quantifies growth over time. It is computed as New Members - Cancelled Members per Period, expressed in count (items per period). Its use is concentrated in Fitness & wellness. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Net member growth measures the change in membership base - new members minus cancels - and it is the fitness business's headline expansion metric, the number that drives revenue growth projections and facility-planning decisions. Net growth is a compound of two opposite-flow processes: acquisition (marketing, sales, referral) and retention (engagement, results, community), and the pair responds to entirely different management levers - which is why reading net growth alone hides whether growth is marketing-fueled (expensive) or retention-fueled (durable). Market-capacity ceiling effects matter: a club approaching its addressable-market saturation shows declining net growth while doing everything right. Read with gross versus net member growth decomposition, member acquisition cost trend, and revenue per member (growth that dilutes monetization is weak growth).

## Formula

```
New Members - Cancelled Members per Period
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** customer
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** fitness_wellness
- **Sector:** fitness_wellness

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1038 (batch 3)
