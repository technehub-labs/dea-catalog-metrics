# dea:metric-scenario-impact-confidence-interval

Candidate Performance Metric record for **Scenario Impact Confidence Interval** (SICI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-scenario-impact-confidence-interval`
- **Name:** Scenario Impact Confidence Interval
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SICI

## 2. Definition

Within Financial Planning & Analysis, Scenario Impact Confidence Interval (SICI) is used to gauge exposure to adverse outcomes. Its calculation is Width of Modeled Outcome Range at Target Confidence, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures how much certainty the scenario analysis can honestly claim. Intervals that are too narrow signal model overconfidence. Confidence computed on historical regimes understates tail behavior. Read with scenario analysis coverage and expected shortfall estimate stability.

## Formula

```
Width of Modeled Outcome Range at Target Confidence
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** financial_planning_analysis

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3784 (batch 8)
