# dea:metric-shop-visit-prediction-accuracy

Candidate Performance Metric record for **Shop Visit Prediction Accuracy** (SVPA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-shop-visit-prediction-accuracy`
- **Name:** Shop Visit Prediction Accuracy
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SVPA

## 2. Definition

Shop Visit Prediction Accuracy (SVPA) captures the quality of outputs and outcomes for organizations tracking aviation maintenance repair & overhaul. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Actual Shop Visits Matched by Forecast / Actual Shop Visits - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Airlines & aviation sector.

## 3. Context

Measures how closely predicted engine or component shop visits match actual removals. It matters because unscheduled visits wreck capacity plans and spare economics. Accuracy can look good if predictions are padded so removals rarely exceed them. Read with Forecast Bias and Unscheduled Removal Rate to confirm predictions are sharp, not safe.

## Formula

```
Actual Shop Visits Matched by Forecast / Actual Shop Visits
```

## Unit

- **Unit reference:** `dea:unit-percent`
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
- **Domain:** aviation_maintenance_repair_overhaul
- **Sector:** airlines_aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1193 (batch 4)
