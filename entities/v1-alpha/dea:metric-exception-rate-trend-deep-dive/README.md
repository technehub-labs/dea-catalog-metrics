# dea:metric-exception-rate-trend-deep-dive

Candidate Performance Metric record for **Exception Rate Trend (Deep Dive)** (ERT-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-exception-rate-trend-deep-dive`
- **Name:** Exception Rate Trend (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ERT-D

## 2. Definition

Exception Rate Trend (Deep Dive) (ERT-D) captures the quality of outputs and outcomes for organizations tracking balanced scorecard - internal process perspective. The formula is Change in Process Exception Rate - reported in percent (%). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
ERT-D = Change in Process Exception Rate
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** balanced_scorecard_internal_process_perspective

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3086 (batch 7)
