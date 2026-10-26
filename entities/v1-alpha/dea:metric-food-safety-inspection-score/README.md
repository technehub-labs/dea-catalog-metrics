# dea:metric-food-safety-inspection-score

Candidate Performance Metric record for **Food Safety Inspection Score** (FSIS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-food-safety-inspection-score`
- **Name:** Food Safety Inspection Score
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FSIS

## 2. Definition

A Restaurants indicator, Food Safety Inspection Score (FSIS) quantifies conformance to standards, plans, or obligations. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Weighted Regulatory Inspection Score, expressed in score (points). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Restaurants.

## 3. Context

Food safety inspection scores come from health department visits, and in restaurants they are the compliance metric with public visibility - many jurisdictions post letter grades or numeric scores at the door and online, and studies have shown measurable revenue impact from grade changes in scored jurisdictions. The distinctive challenge is unscheduled variability: inspections sample one day's operation, so scores reflect both steady-state practice and inspection-day luck. The distributional view is more honest than the average: violation patterns (repeat critical violations on the same item across inspections) reveal systemic process gaps, and critical-versus-noncritical violation separation matters for risk since critical items (temperature control, handwashing) are the illness vectors. Read with repeat-violation analysis, time-between-critical-violations trend, and self-inspection program results as the internal leading indicator.

## Formula

```
Weighted Regulatory Inspection Score
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** customer
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** restaurants
- **Sector:** restaurants

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 939 (batch 3)
