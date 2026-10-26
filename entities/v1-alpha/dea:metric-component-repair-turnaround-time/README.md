# dea:metric-component-repair-turnaround-time

Candidate Performance Metric record for **Component Repair Turnaround Time** (CRTAT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-component-repair-turnaround-time`
- **Name:** Component Repair Turnaround Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CRTAT

## 2. Definition

Within Aviation Maintenance Repair & Overhaul, Component Repair Turnaround Time (CRTAT) is used to gauge how efficiently resources are converted into outputs. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Days from Component Removal to Serviceable Return - reported in days. It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Airlines & aviation sector.

## 3. Context

Measures elapsed time for component repair in MRO operations. It matters because component TAT drives aircraft-on-ground events and inventory of serviceable spares. TAT can be cut by expediting test skips that later surface as field failures. Read with Serviceable Spares Availability and Repeat Defect Rate (Aviation) to confirm speed coexists with quality.

## Formula

```
Days from Component Removal to Serviceable Return
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** aviation_maintenance_repair_overhaul
- **Sector:** airlines_aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1187 (batch 4)
