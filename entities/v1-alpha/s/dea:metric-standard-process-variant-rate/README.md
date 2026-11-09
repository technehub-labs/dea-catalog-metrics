# dea:metric-standard-process-variant-rate

Candidate Performance Metric record for **Standard Process Variant Rate** (SPVR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-standard-process-variant-rate`
- **Name:** Standard Process Variant Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SPVR

## 2. Definition

Standard Process Variant Rate (SPVR) measures governance in the Operating Model & Process Health Deep Dive domain. The formula is Approved Process Variants / Base Processes - reported in ratio (x:1 or x). It is applied across virtually every sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
SPVR = Approved Process Variants / Base Processes
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** transformation
- **Purpose classification:** governance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3507 (batch 7)
