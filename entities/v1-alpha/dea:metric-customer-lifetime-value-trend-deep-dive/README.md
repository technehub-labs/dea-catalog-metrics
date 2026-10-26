# dea:metric-customer-lifetime-value-trend-deep-dive

Candidate Performance Metric record for **Customer Lifetime Value Trend (Deep Dive)** (CLVT-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-customer-lifetime-value-trend-deep-dive`
- **Name:** Customer Lifetime Value Trend (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CLVT-D

## 2. Definition

Customer Lifetime Value Trend (Deep Dive) (CLVT-D) measures the economic value created or preserved in the Balanced Scorecard - Customer Perspective domain. It is computed as Change in CLV between Periods, expressed in currency value. It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the direction of predicted customer value over time. LTV trends reveal whether retention and expansion economics are compounding or eroding. Model optimism (retention assumptions) silently inflates the trend. Read with LTV to CAC ratio and net revenue retention.

## Formula

```
Change in CLV between Periods
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** strategy
- **Purpose classification:** value_delivery
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3071 (batch 7)
