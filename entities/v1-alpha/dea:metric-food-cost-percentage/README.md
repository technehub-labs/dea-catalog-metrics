# dea:metric-food-cost-percentage

Candidate Performance Metric record for **Food Cost Percentage** (FCP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-food-cost-percentage`
- **Name:** Food Cost Percentage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FCP

## 2. Definition

A Hospitality & Food Service indicator, Food Cost Percentage (FCP) quantifies how efficiently resources are converted into outputs. The formula is Food Cost / Food Revenue - reported in percent (%). It is a standard measure in the Hospitality sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures food cost as a share of food sales in food service operations. It matters because it is the primary controllable profit lever in kitchens. Teams can cut it by shrinking portions or substituting cheaper ingredients, both of which surface in satisfaction. Read with Menu Item Margin Mix and Guest Satisfaction to confirm cost control is not eating quality.

## Formula

```
FCP = Food Cost / Food Revenue
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** hospitality_food_service
- **Sector:** hospitality

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 509 (batch 1)
