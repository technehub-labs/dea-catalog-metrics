# dea:metric-model-drift-alert-response-time

Candidate Performance Metric record for **Model Drift Alert Response Time** (MDART) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-model-drift-alert-response-time`
- **Name:** Model Drift Alert Response Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MDART

## 2. Definition

A AI Governance & Model Risk Management indicator, Model Drift Alert Response Time (MDART) quantifies how efficiently resources are converted into outputs. It is computed as Hours from Drift Alert to Acknowledged Action, expressed in hours. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Hours from Drift Alert to Acknowledged Action
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** governance
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** ai_governance_model_risk_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2510 (batch 7)
