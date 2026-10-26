# dea:metric-single-reviewer-change-ratio

Candidate Performance Metric record for **Single-Reviewer Change Ratio** (SRCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-single-reviewer-change-ratio`
- **Name:** Single-Reviewer Change Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SRCR

## 2. Definition

Within Code Review & Peer Quality, Single-Reviewer Change Ratio (SRCR) is used to gauge exposure to adverse outcomes. It provides the day-to-day signal that a process is running as designed. Its calculation is Changes Approved by One Reviewer / Merged Changes, measured in percent (%). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Software practice.

## Formula

```
Changes Approved by One Reviewer / Merged Changes
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3191 (batch 7)
