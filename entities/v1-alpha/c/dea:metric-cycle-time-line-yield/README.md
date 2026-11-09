# dea:metric-cycle-time-line-yield

Candidate Performance Metric record for **Cycle Time Line Yield** (CTLY) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cycle-time-line-yield`
- **Name:** Cycle Time Line Yield
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CTLY

## 2. Definition

Cycle Time Line Yield (CTLY) addresses the quality of outputs and outcomes and is a fixture of semiconductor & electronics reporting. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Units Completing All Process Steps / Units Started, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Electronics & semiconductors.

## 3. Context

Measures the compound of wafer fabrication cycle time and line yield. It matters because long cycle times with poor yield create compounding cost and capacity drag. Yield can be flattered by excluding engineering lots or scrap reclassification. Read with Scrap Cost per Wafer and On-Time Delivery (Semiconductor) to confirm performance is end-to-end.

## Formula

```
CTLY = Units Completing All Process Steps / Units Started
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
- **Domain:** semiconductor_electronics
- **Sector:** electronics_semiconductors

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 909 (batch 3)
