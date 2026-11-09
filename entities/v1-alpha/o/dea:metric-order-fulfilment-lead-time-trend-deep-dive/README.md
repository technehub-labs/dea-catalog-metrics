# dea:metric-order-fulfilment-lead-time-trend-deep-dive

Candidate Performance Metric record for **Order Fulfilment Lead Time Trend (Deep Dive)** (OFLTT-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-order-fulfilment-lead-time-trend-deep-dive`
- **Name:** Order Fulfilment Lead Time Trend (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** OFLTT-D

## 2. Definition

Order Fulfilment Lead Time Trend (Deep Dive) (OFLTT-D) measures how efficiently resources are converted into outputs in the Balanced Scorecard - Internal Process Perspective domain. The formula is Change in Fulfilment Lead Time - reported in days. It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the direction of time from order to customer receipt. Lead time is the operational promise the brand makes, and its trend predicts competitive durability. Averaging across product lines hides the SKUs customers actually complain about. Read with perfect order rate and process cycle time trend.

## Formula

```
OFLTT-D = Change in Fulfilment Lead Time
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** strategy
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** balanced_scorecard_internal_process_perspective

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3091 (batch 7)
