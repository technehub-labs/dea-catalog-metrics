# dea:metric-recovery-point-objective-attainment-deep-dive

Candidate Performance Metric record for **Recovery Point Objective Attainment (Deep Dive)** (RPOA-SA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-recovery-point-objective-attainment-deep-dive`
- **Name:** Recovery Point Objective Attainment (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RPOA-SA

## 2. Definition

A Software Architecture & Technical Design indicator, Recovery Point Objective Attainment (Deep Dive) (RPOA-SA) quantifies exposure to adverse outcomes. It is computed as Data Loss within RPO / Loss Events, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures whether data loss stayed within tolerance in actual incidents. It is the data-integrity twin of RTO: systems that restore quickly with stale or corrupted data have technically recovered and practically failed. Attainment verification requires restoring and validating actual data, not restarting services. Read with backup verification coverage and restore-test success rates.

## Formula

```
Data Loss within RPO / Loss Events
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2632 (batch 7)
