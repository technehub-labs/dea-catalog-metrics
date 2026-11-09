# dea:metric-customer-satisfaction-score-trend-deep-dive

Candidate Performance Metric record for **Customer Satisfaction Score Trend (Deep Dive)** (CSATT-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-customer-satisfaction-score-trend-deep-dive`
- **Name:** Customer Satisfaction Score Trend (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CSATT-D

## 2. Definition

Within Balanced Scorecard - Customer Perspective, Customer Satisfaction Score Trend (Deep Dive) (CSATT-D) is used to gauge the engagement or satisfaction of the people involved. It is computed as Change in CSAT between Periods, expressed in score (points). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the direction of customer satisfaction over time. The trend is more diagnostic than the level: declining satisfaction in a period of growth signals scaling strain. Satisfaction can stay high while switching behavior accelerates. Read with net promoter score movement and churn rate.

## Formula

```
CSATT-D = Change in CSAT between Periods
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3066 (batch 7)
