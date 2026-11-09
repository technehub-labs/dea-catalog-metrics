# dea:metric-process-capability-index

Candidate Performance Metric record for **Process Capability Index** (Cpk) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-process-capability-index`
- **Name:** Process Capability Index
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** Cpk

## 2. Definition

Process Capability Index (Cpk) captures the quality of outputs and outcomes for organizations tracking quality management. The formula is min(USL - Mean, Mean - LSL) / (3 x Std Dev) - reported in ratio (x:1 or x). It is applied across virtually every sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how well a process output fits within specification limits relative to its natural variation. It matters because capable processes produce quality without inspection-heavy control. Gaming risk includes widening specification limits with customers or cherry-picking stable periods for measurement. Read with First Pass Yield and Defect Density to confirm capability matches observed defect performance.

## Formula

```
Cpk = min(USL - Mean, Mean - LSL) / (3 x Std Dev)
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** capability
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** quality_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 240 (batch 1)
