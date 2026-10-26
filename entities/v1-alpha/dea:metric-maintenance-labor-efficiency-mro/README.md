# dea:metric-maintenance-labor-efficiency-mro

Candidate Performance Metric record for **Maintenance Labor Efficiency (MRO)** (MLE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-maintenance-labor-efficiency-mro`
- **Name:** Maintenance Labor Efficiency (MRO)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MLE

## 2. Definition

Within Aviation Maintenance Repair & Overhaul, Maintenance Labor Efficiency (MRO) (MLE) is used to gauge how efficiently resources are converted into outputs. Its calculation is Standard Labor Hours / Actual Labor Hours, measured in ratio (x:1 or x). Its value drives prioritization and resource reallocation among competing initiatives. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Airlines & aviation practice.

## 3. Context

Measures labor hours consumed per maintenance task or work package. It matters because MRO margins hinge on labor productivity against quoted hours. Quoted-hour padding makes efficiency look structurally good. Read with Task Rework Rate and quote accuracy variance to confirm efficiency reflects genuine productivity.

## Formula

```
Standard Labor Hours / Actual Labor Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** aviation_maintenance_repair_overhaul
- **Sector:** airlines_aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1190 (batch 4)
