# dea:metric-simulation-correlation-accuracy

Candidate Performance Metric record for **Simulation Correlation Accuracy** (SCA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-simulation-correlation-accuracy`
- **Name:** Simulation Correlation Accuracy
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SCA

## 2. Definition

A Engineering & Design indicator, Simulation Correlation Accuracy (SCA) quantifies the quality of outputs and outcomes. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Model Prediction Error vs Test Data; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how closely simulation models (CAE, digital twins) predict physical test results. It is the enabling metric of virtual-first development: correlation determines how much physical testing can be replaced, and poor correlation silently corrupts design decisions made on model confidence. Track by load case and component class, since correlation quality varies systematically. Read with physical test reduction achieved and late-stage design changes discovered in test.

## Formula

```
SCA = Model Prediction Error vs Test Data
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** engineering_design

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1768 (batch 6)
