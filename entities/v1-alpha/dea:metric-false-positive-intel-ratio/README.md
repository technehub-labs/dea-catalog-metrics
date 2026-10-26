# dea:metric-false-positive-intel-ratio

Candidate Performance Metric record for **False Positive Intel Ratio** (FPIR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-false-positive-intel-ratio`
- **Name:** False Positive Intel Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FPIR

## 2. Definition

A Threat Intelligence & Red Team indicator, False Positive Intel Ratio (FPIR) quantifies the quality of outputs and outcomes. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Intel Items Disproven / Items Actioned - reported in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Intel Items Disproven / Items Actioned
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** threat_intelligence_red_team

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3290 (batch 7)
