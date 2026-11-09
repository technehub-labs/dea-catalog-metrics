# dea:metric-escalation-layer-depth

Candidate Performance Metric record for **Escalation Layer Depth** (ELD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-escalation-layer-depth`
- **Name:** Escalation Layer Depth
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ELD

## 2. Definition

A Operating Model & Process Health Deep Dive indicator, Escalation Layer Depth (ELD) quantifies how efficiently resources are converted into outputs. Its calculation is Layers Required to Resolve Standard Escalation, measured in count (items per period). Its value drives prioritization and resource reallocation among competing initiatives. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
ELD = Layers Required to Resolve Standard Escalation
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** transformation
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** operating_model_process_health_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3500 (batch 7)
