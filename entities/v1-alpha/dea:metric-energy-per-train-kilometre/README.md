# dea:metric-energy-per-train-kilometre

Candidate Performance Metric record for **Energy per Train Kilometre** (EPKM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-energy-per-train-kilometre`
- **Name:** Energy per Train Kilometre
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** EPKM

## 2. Definition

A Rail Transport indicator, Energy per Train Kilometre (EPKM) quantifies how efficiently resources are converted into outputs. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Energy Consumed / Train Kilometres - reported in ratio (x:1 or x). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Rail sector.

## 3. Context

Measures traction energy consumed per kilometer operated. It matters because energy is the largest controllable cost in rail operations and a direct emissions lever. Mixed traffic profiles (freight vs passenger) can distort comparisons unless normalized. Read with Load Factor and Punctuality to confirm efficiency gains do not come from lighter loads or slower running.

## Formula

```
Energy Consumed / Train Kilometres
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** rail_transport
- **Sector:** rail

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 999 (batch 3)
