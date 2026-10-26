# dea:metric-stale-review-abandonment-rate

Candidate Performance Metric record for **Stale Review Abandonment Rate** (SRAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-stale-review-abandonment-rate`
- **Name:** Stale Review Abandonment Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SRAR

## 2. Definition

Stale Review Abandonment Rate (SRAR) addresses how efficiently resources are converted into outputs and is a fixture of code review & peer quality reporting. It is computed as Open Reviews Abandoned / Opened Reviews, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Lower values are better; each reduction is an improvement. Its use is concentrated in Software.

## Formula

```
Open Reviews Abandoned / Opened Reviews
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** code_review_peer_quality
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3201 (batch 7)
