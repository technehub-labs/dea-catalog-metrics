# dea:metric-derailment-rate-per-million-train-kilometres-deep-dive

Candidate Performance Metric record for **Derailment Rate per Million Train Kilometres (Deep Dive)** (DRMTK) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-derailment-rate-per-million-train-kilometres-deep-dive`
- **Name:** Derailment Rate per Million Train Kilometres (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DRMTK

## 2. Definition

A Rail Freight (Deep Dive) indicator, Derailment Rate per Million Train Kilometres (Deep Dive) (DRMTK) quantifies exposure to adverse outcomes. It is computed as Derailments / Million Train Kilometres, expressed in events per thousand or million (scaled). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is concentrated in Rail.

## 3. Context

Measures derailments normalized by train distance. It is the safety-core metric of rail operations, and it is scrutinized by regulators and insurers alike because derailment severity concentrates (hazardous materials, mainline speeds) into catastrophic outcomes. Rate reduction from traffic mix shifts (fewer hazmat trains) is portfolio change, not safety improvement. Read with track-defect detection trends and broken-rail prevention program effectiveness.

## Formula

```
Derailments / Million Train Kilometres
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** rail_freight_deep_dive
- **Sector:** rail

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2425 (batch 6)
