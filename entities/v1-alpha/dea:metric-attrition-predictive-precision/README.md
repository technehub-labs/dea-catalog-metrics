# dea:metric-attrition-predictive-precision

Candidate Performance Metric record for **Attrition Predictive Precision** (APP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-attrition-predictive-precision`
- **Name:** Attrition Predictive Precision
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** APP

## 2. Definition

Attrition Predictive Precision (APP) captures the quality of outputs and outcomes for organizations tracking workforce planning & analytics. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is True At-Risk Departures Predicted / Predicted Departures, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how accurately attrition models predict actual leavers. It matters because save-action programs are only as good as their targeting. Precision can look strong on easy-to-predict segments while missing surprises. Read with Attrition Cost saved per intervention and model recall on unexpected exits to confirm predictions are useful.

## Formula

```
APP = True At-Risk Departures Predicted / Predicted Departures
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** workforce_planning_analytics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1456 (batch 5)
