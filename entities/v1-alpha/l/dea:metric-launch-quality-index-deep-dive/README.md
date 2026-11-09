# dea:metric-launch-quality-index-deep-dive

Candidate Performance Metric record for **Launch Quality Index (Deep Dive)** (LQI-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-launch-quality-index-deep-dive`
- **Name:** Launch Quality Index (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** LQI-D

## 2. Definition

Launch Quality Index (Deep Dive) (LQI-D) captures the quality of outputs and outcomes for organizations tracking automotive manufacturing (deep dive). Its calculation is Composite New-Launch Defect Score, measured in index (0-100 or normalized). It originates from and is most used in Automotive practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

A composite of launch-phase quality measures - early warranty rates, containment actions, ramp defects, customer-reported issues in the first months. Launch quality determines both launch economics (containment labor, hold lots, missed volumes) and the model's lifetime reputation, and it is where automotive reputations are quietly won and lost. Compare launches against maturation benchmarks, not absolute values. Read with first time through - assembly (Deep Dive) and warranty early-warning indicators.

## Formula

```
LQI-D = Composite New-Launch Defect Score
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** automotive_manufacturing_deep_dive
- **Sector:** automotive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2368 (batch 6)
