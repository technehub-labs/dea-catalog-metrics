# dea:metric-comment-to-code-ratio

Candidate Performance Metric record for **Comment-to-Code Ratio** (CCR-CQ) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-comment-to-code-ratio`
- **Name:** Comment-to-Code Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CCR-CQ

## 2. Definition

Within Code Quality & Static Analysis, Comment-to-Code Ratio (CCR-CQ) is used to gauge the quality of outputs and outcomes. It is defined as Comment Lines / Code Lines; the result is stated in percent (%). In Software, it is a recognized element of the standard performance toolkit. It is a working-level control: thresholds trigger immediate operational response. Values outside the intended band, on either side, warrant investigation.

## Formula

```
CCR-CQ = Comment Lines / Code Lines
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** code_quality_static_analysis
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4184 (batch 9)
