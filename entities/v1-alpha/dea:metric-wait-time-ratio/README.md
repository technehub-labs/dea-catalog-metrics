# dea:metric-wait-time-ratio

Candidate Performance Metric record for **Wait Time Ratio** (WTR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-wait-time-ratio`
- **Name:** Wait Time Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** WTR

## 2. Definition

Wait Time Ratio (WTR) addresses how efficiently resources are converted into outputs and is a fixture of process excellence (lean six sigma) reporting. The formula is Waiting Time / Total Process Lead Time - reported in percent (%). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of process lead time customers or items spend waiting. It matters because wait is the dominant, least-loved component of most service processes. Waits can be hidden by quoting lead times that already bake waiting into promises. Read with Value-Added Time Ratio and Average Handle Time to locate where queues actually form.

## Formula

```
Waiting Time / Total Process Lead Time
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** capability
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** process_excellence_lean_six_sigma

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1114 (batch 4)
