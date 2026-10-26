# dea:metric-supplier-ppm-automotive

Candidate Performance Metric record for **Supplier PPM (Automotive)** (SPPM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-supplier-ppm-automotive`
- **Name:** Supplier PPM (Automotive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SPPM

## 2. Definition

Supplier PPM (Automotive) (SPPM) captures the quality of outputs and outcomes for organizations tracking automotive. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Defective Supplier Parts per Million Parts Received - reported in events per thousand or million (scaled). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Automotive sector.

## 3. Context

Measures defective parts per million received from suppliers. It matters because assembly lines stop for supplier defects, and warranty cost traces to component quality. Suppliers can reduce counted PPM through containment sorting, hiding the true defect rate. Read with Supplier Quality Rating and Line Stop Rate attributable to suppliers to confirm PPM reflects the full flow.

## Formula

```
Defective Supplier Parts per Million Parts Received
```

## Unit

- **Unit reference:** `dea:unit-events`
- **Unit:** events
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** automotive
- **Sector:** automotive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 742 (batch 2)
