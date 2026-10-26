# dea:metric-marketing-attributed-revenue

Candidate Performance Metric record for **Marketing Attributed Revenue** (MAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-marketing-attributed-revenue`
- **Name:** Marketing Attributed Revenue
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MAR

## 2. Definition

Within Marketing, Marketing Attributed Revenue (MAR) is used to gauge the economic value created or preserved. It is computed as Revenue from Marketing-Touched Conversions, expressed in currency value. It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The revenue that attribution models assign to marketing activity - the bridge metric between marketing spend and the P&L, and simultaneously the most demanded and most abused number in the marketing stack. Every attribution model - last touch, multi-touch, linear, time-decay, algorithmic - embodies a theory of causation, and switching models reallocates the same revenue without changing any customer behavior. Strategic use is directional and consistent: pick a model, hold it fixed, and read trends, because the trend under one model is informative while the level across models is not. The gold standard remains incrementality testing against the attributed number, and the gap between the two is a direct measure of how much the attribution model flatters marketing.

## Formula

```
Revenue from Marketing-Touched Conversions
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** marketing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 120 (batch 1)
