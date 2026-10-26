# dea:metric-ingredient-waste-rate

Candidate Performance Metric record for **Ingredient Waste Rate** (IWR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ingredient-waste-rate`
- **Name:** Ingredient Waste Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** IWR

## 2. Definition

Within Restaurants, Ingredient Waste Rate (IWR) is used to gauge how efficiently resources are converted into outputs. Its calculation is Wasted Ingredient Value / Ingredient Value Used, measured in percent (%). It originates from and is most used in Restaurants practice. It provides the day-to-day signal that a process is running as designed. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
IWR = Wasted Ingredient Value / Ingredient Value Used
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
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** restaurants
- **Sector:** restaurants

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 945 (batch 3)
