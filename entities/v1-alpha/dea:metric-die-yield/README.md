# dea:metric-die-yield

Candidate Performance Metric record for **Die Yield** (DIEY) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-die-yield`
- **Name:** Die Yield
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DIEY

## 2. Definition

Die Yield (DIEY) captures the quality of outputs and outcomes for organizations tracking semiconductor & electronics. Its calculation is Functional Die per Wafer / Total Die per Wafer, measured in percent (%). It originates from and is most used in Electronics & semiconductors practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Die yield measures the share of dies on a wafer that pass electrical test - the single most economically consequential metric in semiconductor manufacturing, since yield directly translates to wafer revenue and a few points of yield on an advanced node are worth enormous sums per fab per year. Yield is a defectivity and design problem at once: process-induced defects, lithographic variations, and design marginality all contribute, and yield learning follows predictable but unforgiving ramp curves per node. Mature nodes can run above 90 percent while leading-edge nodes launch far lower and climb. Yield decomposition drives improvement: systematic (fixed pattern) versus random (defect-limited) yield loss require different engineering responses. Read with defect density trend, yield by product versus by process step, and yield-learning-curve position against node maturity.

## Formula

```
Functional Die per Wafer / Total Die per Wafer
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
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** semiconductor_electronics
- **Sector:** electronics_semiconductors

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 904 (batch 3)
