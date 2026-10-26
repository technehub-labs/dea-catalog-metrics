# dea:metric-review-to-merge-elapsed-time

Candidate Performance Metric record for **Review-to-Merge Elapsed Time** (RMET) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-review-to-merge-elapsed-time`
- **Name:** Review-to-Merge Elapsed Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RMET

## 2. Definition

Review-to-Merge Elapsed Time (RMET) captures how efficiently resources are converted into outputs for organizations tracking code review & peer quality. It is computed as Median Hours from Review Start to Merge, expressed in hours. Its use is concentrated in Software. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Median Hours from Review Start to Merge
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3202 (batch 7)
