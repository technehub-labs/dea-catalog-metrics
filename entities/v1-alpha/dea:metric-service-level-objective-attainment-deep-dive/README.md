# dea:metric-service-level-objective-attainment-deep-dive

Candidate Performance Metric record for **Service Level Objective Attainment (Deep Dive)** (SLOA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-service-level-objective-attainment-deep-dive`
- **Name:** Service Level Objective Attainment (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SLOA

## 2. Definition

Service Level Objective Attainment (Deep Dive) (SLOA) captures the quality of outputs and outcomes for organizations tracking sre & observability standard measures. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Windows Meeting SLO / Total Windows, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Software.

## 3. Context

Measures whether services met their SLOs over the window. SLO attainment is the reliability contract between engineering and product. Attainment measured on technically convenient windows (calendar month) can hide painful intra-window gaps. Read with service level objective attainment and error budget remaining.

## Formula

```
Windows Meeting SLO / Total Windows
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sre_observability_standard_measures
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4377 (batch 11)
