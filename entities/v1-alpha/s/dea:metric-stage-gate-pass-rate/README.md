# dea:metric-stage-gate-pass-rate

Candidate Performance Metric record for **Stage-Gate Pass Rate** (SGPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-stage-gate-pass-rate`
- **Name:** Stage-Gate Pass Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SGPR

## 2. Definition

A R&D and Innovation indicator, Stage-Gate Pass Rate (SGPR) quantifies the quality of outputs and outcomes. Its calculation is Concepts Passing Gate / Concepts Reviewed, measured in percent (%). It is applied across virtually every sector. Its value drives prioritization and resource reallocation among competing initiatives. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of R&D projects passing each development gate on first presentation. It matters because it reflects portfolio discipline and the honesty of gate criteria. Teams can inflate it by passing projects with conditions that are never enforced, or by softening gate criteria after the fact. Read with Project Kill Rate and New Product Success Rate to confirm gates actually filter rather than rubber-stamp.

## Formula

```
SGPR = Concepts Passing Gate / Concepts Reviewed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** r_d_and_innovation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 542 (batch 1)
