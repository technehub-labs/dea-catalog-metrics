# dea:metric-member-visits-per-month

Candidate Performance Metric record for **Member Visits per Month** (MVM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-member-visits-per-month`
- **Name:** Member Visits per Month
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MVM

## 2. Definition

Member Visits per Month (MVM) measures the engagement or satisfaction of the people involved in the Fitness & Wellness domain. The formula is Total Visits / Average Members - reported in ratio (x:1 or x). It is a standard measure in the Fitness & wellness sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures average visits per gym member. It matters because visit frequency is the behavioral predictor of retention in fitness. Check-in games and challenges can spike visits without habit formation. Read with Member Churn Rate and Personal Training Attach Rate to confirm frequency converts to loyalty.

## Formula

```
MVM = Total Visits / Average Members
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** customer
- **Purpose classification:** engagement
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** fitness_wellness
- **Sector:** fitness_wellness

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1034 (batch 3)
