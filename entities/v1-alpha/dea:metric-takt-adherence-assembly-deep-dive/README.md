# dea:metric-takt-adherence-assembly-deep-dive

Candidate Performance Metric record for **Takt Adherence (Assembly Deep Dive)** (TA-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-takt-adherence-assembly-deep-dive`
- **Name:** Takt Adherence (Assembly Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TA-D

## 2. Definition

Within Automotive Manufacturing (Deep Dive), Takt Adherence (Assembly Deep Dive) (TA-D) is used to gauge how efficiently resources are converted into outputs. It is defined as Stations Completing within Takt / Stations; the result is stated in percent (%). It is a working-level control: thresholds trigger immediate operational response. Higher values are better; gains are read as improvement and losses as deterioration. In Automotive, it is a recognized element of the standard performance toolkit.

## Formula

```
Stations Completing within Takt / Stations
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** automotive_manufacturing_deep_dive
- **Sector:** automotive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2365 (batch 6)
