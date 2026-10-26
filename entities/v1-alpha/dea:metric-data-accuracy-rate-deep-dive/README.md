# dea:metric-data-accuracy-rate-deep-dive

Candidate Performance Metric record for **Data Accuracy Rate (Deep Dive)** (DAR-DQ) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-accuracy-rate-deep-dive`
- **Name:** Data Accuracy Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DAR-DQ

## 2. Definition

Data Accuracy Rate (Deep Dive) (DAR-DQ) addresses the quality of outputs and outcomes and is a fixture of data quality management reporting. It is computed as Values Matching Verified Source / Values Sampled, expressed in percent (%). It is applied across virtually every sector. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
DAR-DQ = Values Matching Verified Source / Values Sampled
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** data_quality_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3616 (batch 8)
