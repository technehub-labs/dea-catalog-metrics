# dea:metric-net-promoter-score-movement-deep-dive

Candidate Performance Metric record for **Net Promoter Score Movement (Deep Dive)** (NPSM-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-net-promoter-score-movement-deep-dive`
- **Name:** Net Promoter Score Movement (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** NPSM-D

## 2. Definition

Within Balanced Scorecard - Customer Perspective, Net Promoter Score Movement (Deep Dive) (NPSM-D) is used to gauge the engagement or satisfaction of the people involved. Its calculation is NPS Change between Periods, measured in score (points). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the change in NPS rather than its level. Movement isolates the effect of recent initiatives from the accumulated brand baseline. Small-sample swings are noise that invites overreaction. Read with customer satisfaction score trend and customer effort score.

## Formula

```
NPSM-D = NPS Change between Periods
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** engagement
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** balanced_scorecard_customer_perspective

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3067 (batch 7)
