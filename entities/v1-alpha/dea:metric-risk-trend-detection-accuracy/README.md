# dea:metric-risk-trend-detection-accuracy

Candidate Performance Metric record for **Risk Trend Detection Accuracy** (RTDA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-risk-trend-detection-accuracy`
- **Name:** Risk Trend Detection Accuracy
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RTDA

## 2. Definition

Risk Trend Detection Accuracy (RTDA) captures the quality of outputs and outcomes for organizations tracking project risk & issue management. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Leading Indicators Predicting Risk / Leading Indicators; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures whether the risks that later materialized had been flagged and trending in advance. Detection accuracy evaluates the risk process, not the risk appetite. Accuracy computed only on materialized risks ignores false alarms that consumed effort. Read with risk exposure trend index (Projects) and root cause analysis completion rate.

## Formula

```
Leading Indicators Predicting Risk / Leading Indicators
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** project_risk_issue_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3432 (batch 7)
