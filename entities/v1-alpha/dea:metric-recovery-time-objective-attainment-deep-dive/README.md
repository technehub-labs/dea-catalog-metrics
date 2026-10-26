# dea:metric-recovery-time-objective-attainment-deep-dive

Candidate Performance Metric record for **Recovery Time Objective Attainment (Deep Dive)** (RTOA-SA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-recovery-time-objective-attainment-deep-dive`
- **Name:** Recovery Time Objective Attainment (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RTOA-SA

## 2. Definition

Recovery Time Objective Attainment (Deep Dive) (RTOA-SA) captures exposure to adverse outcomes for organizations tracking software architecture & technical design. The formula is Actual Recovery Time within RTO / Recovery Events - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures whether critical systems restored within target recovery times in actual incidents and failover tests. RTO attainment is where resilience planning meets physics: many well-documented RTOs fail on test, and untested attainment is aspiration. Measure from disruption onset, not declaration, and test the full dependency chain since partial restoration is not attainment. Read with recovery point objective attainment (Deep Dive) and disaster recovery test results.

## Formula

```
Actual Recovery Time within RTO / Recovery Events
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** software_architecture_technical_design

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2631 (batch 7)
