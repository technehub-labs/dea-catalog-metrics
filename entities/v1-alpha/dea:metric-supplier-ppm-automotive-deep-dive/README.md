# dea:metric-supplier-ppm-automotive-deep-dive

Candidate Performance Metric record for **Supplier PPM - Automotive (Deep Dive)** (SPPM-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-supplier-ppm-automotive-deep-dive`
- **Name:** Supplier PPM - Automotive (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SPPM-D

## 2. Definition

Supplier PPM - Automotive (Deep Dive) (SPPM-D) captures the quality of outputs and outcomes for organizations tracking automotive manufacturing (deep dive). Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Defective Parts per Million Received; the result is stated in events per thousand or million (scaled). It should be driven down, since lower readings signal healthier performance. In Automotive, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures defective parts per million from suppliers. In a just-in-time industry, supplier defect rates translate directly into line stoppage risk, containment cost, and field quality, and PPM is the shared language of automotive supplier management. PPM must be read with severity - a defective seat fabric and a defective brake component are not the same PPM. Read with supplier launch quality and warranty attribution analysis.

## Formula

```
Defective Parts per Million Received
```

## Unit

- **Unit reference:** `dea:unit-events`
- **Unit:** events
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** automotive_manufacturing_deep_dive
- **Sector:** automotive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2369 (batch 6)
