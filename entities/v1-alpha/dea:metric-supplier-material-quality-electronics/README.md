# dea:metric-supplier-material-quality-electronics

Candidate Performance Metric record for **Supplier Material Quality (Electronics)** (SMQ) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-supplier-material-quality-electronics`
- **Name:** Supplier Material Quality (Electronics)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SMQ

## 2. Definition

Supplier Material Quality (Electronics) (SMQ) addresses the quality of outputs and outcomes and is a fixture of semiconductor & electronics reporting. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Incoming Lots Meeting Specification / Lots Received; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. In Electronics & semiconductors, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures incoming material quality from electronics suppliers. It matters because contaminated or defective materials propagate into yields across the entire production chain. Sampling-based acceptance can miss lot-level defects that later escape. Read with Supplier PPM trends and Line Yield Impact to confirm supplier quality holds at volume.

## Formula

```
SMQ = Incoming Lots Meeting Specification / Lots Received
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 914 (batch 3)
