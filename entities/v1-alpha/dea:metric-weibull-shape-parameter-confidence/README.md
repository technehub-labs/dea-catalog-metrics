# dea:metric-weibull-shape-parameter-confidence

Candidate Performance Metric record for **Weibull Shape Parameter Confidence** (WSPC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-weibull-shape-parameter-confidence`
- **Name:** Weibull Shape Parameter Confidence
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** WSPC

## 2. Definition

A Reliability & Maintainability Engineering (Deep Dive) indicator, Weibull Shape Parameter Confidence (WSPC) quantifies the quality of outputs and outcomes. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Confidence Interval Width of Fitted Beta, expressed in ratio (x:1 or x). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Confidence Interval Width of Fitted Beta
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** capability
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** reliability_maintainability_engineering_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4097 (batch 9)
