# dea:metric-distributed-trace-sampling-efficiency

Candidate Performance Metric record for **Distributed Trace Sampling Efficiency** (DTSE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-distributed-trace-sampling-efficiency`
- **Name:** Distributed Trace Sampling Efficiency
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DTSE

## 2. Definition

Distributed Trace Sampling Efficiency (DTSE) addresses how efficiently resources are converted into outputs and is a fixture of sre & observability standard measures reporting. It is computed as Trace Samples Retained within Budget while Meeting Diagnostic Need, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Software.

## Formula

```
Trace Samples Retained within Budget while Meeting Diagnostic Need
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sre_observability_standard_measures
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4383 (batch 11)
