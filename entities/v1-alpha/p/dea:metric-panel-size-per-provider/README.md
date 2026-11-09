# dea:metric-panel-size-per-provider

Candidate Performance Metric record for **Panel Size per Provider** (PSP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-panel-size-per-provider`
- **Name:** Panel Size per Provider
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PSP

## 2. Definition

Panel Size per Provider (PSP) addresses the utilization or availability of capacity and is a fixture of medical practice & clinical operations reporting. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Active Patients / Full-Time Provider - reported in count (items per period). The objective is neither maximization nor minimization but staying within an agreed operating band. It is a standard measure in the Healthcare sector.

## Formula

```
PSP = Active Patients / Full-Time Provider
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** medical_practice_clinical_operations
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1638 (batch 6)
