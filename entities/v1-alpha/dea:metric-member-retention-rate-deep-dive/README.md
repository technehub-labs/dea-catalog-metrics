# dea:metric-member-retention-rate-deep-dive

Candidate Performance Metric record for **Member Retention Rate (Deep Dive)** (MRR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-member-retention-rate-deep-dive`
- **Name:** Member Retention Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MRR-D

## 2. Definition

A Fitness & Wellness (Deep Dive) indicator, Member Retention Rate (Deep Dive) (MRR-D) quantifies the retention of customers, users, or assets over time. Its calculation is Members Retained over Period / Start Members, measured in percent (%). It originates from and is most used in Health & Fitness practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of gym or studio members remaining over a period. Retention is the profit engine of fitness: acquisition costs are high, and the business model runs on members who pay longer than they attend. Contract-structure effects (annual versus monthly) distort comparisons, so normalize by commitment type. Read with member visits per month (Deep Dive) as the behavioral predictor.

## Formula

```
Members Retained over Period / Start Members
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** retention
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** fitness_wellness_deep_dive
- **Sector:** health_fitness

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2009 (batch 6)
