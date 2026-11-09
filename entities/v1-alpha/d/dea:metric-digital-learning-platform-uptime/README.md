# dea:metric-digital-learning-platform-uptime

Candidate Performance Metric record for **Digital Learning Platform Uptime** (DLPU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-digital-learning-platform-uptime`
- **Name:** Digital Learning Platform Uptime
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DLPU

## 2. Definition

Digital Learning Platform Uptime (DLPU) measures the utilization or availability of capacity in the Education & Training (Deep Dive) domain. The formula is Platform Available Hours / Required Hours - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Education sector.

## Formula

```
DLPU = Platform Available Hours / Required Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** capability
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** education_training_deep_dive
- **Sector:** education

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2070 (batch 6)
