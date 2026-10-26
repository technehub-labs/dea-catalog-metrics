# dea:metric-afferent-coupling-fan-in

Candidate Performance Metric record for **Afferent Coupling (Fan-In)** (AFFC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-afferent-coupling-fan-in`
- **Name:** Afferent Coupling (Fan-In)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** AFFC

## 2. Definition

Within Code Quality & Static Analysis, Afferent Coupling (Fan-In) (AFFC) is used to gauge the quality of outputs and outcomes. It is computed as Inbound Dependencies per Module, expressed in count (items per period). Its use is concentrated in Software. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Values outside the intended band, on either side, warrant investigation.

## Formula

```
Inbound Dependencies per Module
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** code_quality_static_analysis
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4180 (batch 9)
