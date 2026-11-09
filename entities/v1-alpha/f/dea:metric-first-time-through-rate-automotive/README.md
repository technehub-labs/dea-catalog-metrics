# dea:metric-first-time-through-rate-automotive

Candidate Performance Metric record for **First Time Through Rate (Automotive)** (FTT-A) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-first-time-through-rate-automotive`
- **Name:** First Time Through Rate (Automotive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FTT-A

## 2. Definition

First Time Through Rate (Automotive) (FTT-A) addresses the quality of outputs and outcomes and is a fixture of automotive reporting. It is computed as Vehicles Passing All Inspections without Rework / Vehicles Produced, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Automotive.

## 3. Context

Measures the share of vehicles or units passing through production without rework. It matters because automotive margins depend on catching defects in-station, not at end-of-line. Teams can inflate it by reclassifying in-station repairs as part of standard process. Read with Defects per Vehicle and Warranty Claim trends to confirm first-time quality survives to the customer.

## Formula

```
FTT-A = Vehicles Passing All Inspections without Rework / Vehicles Produced
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** automotive
- **Sector:** automotive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 739 (batch 2)
