# dea:metric-cross-functional-dependency-count

Candidate Performance Metric record for **Cross-Functional Dependency Count** (CFDC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cross-functional-dependency-count`
- **Name:** Cross-Functional Dependency Count
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CFDC

## 2. Definition

Within Operating Model & Process Health Deep Dive, Cross-Functional Dependency Count (CFDC) is used to gauge how efficiently resources are converted into outputs. It is computed as Process Dependencies Crossing Function Boundaries / Process, expressed in ratio (x:1 or x). It is reviewed at cadence by planning owners to correct course before issues become strategic. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Process Dependencies Crossing Function Boundaries / Process
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3506 (batch 7)
