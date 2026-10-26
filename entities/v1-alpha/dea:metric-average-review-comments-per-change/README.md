# dea:metric-average-review-comments-per-change

Candidate Performance Metric record for **Average Review Comments per Change** (ARCC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-review-comments-per-change`
- **Name:** Average Review Comments per Change
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ARCC

## 2. Definition

Average Review Comments per Change (ARCC) captures the quality of outputs and outcomes for organizations tracking code review & peer quality. It is computed as Review Comments / Merged Changes, expressed in ratio (x:1 or x). Its use is concentrated in Software. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Values outside the intended band, on either side, warrant investigation.

## Formula

```
Review Comments / Merged Changes
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** code_review_peer_quality
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3189 (batch 7)
