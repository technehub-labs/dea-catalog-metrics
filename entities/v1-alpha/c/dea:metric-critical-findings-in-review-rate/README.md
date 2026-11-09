# dea:metric-critical-findings-in-review-rate

Candidate Performance Metric record for **Critical Findings in Review Rate** (CFRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-critical-findings-in-review-rate`
- **Name:** Critical Findings in Review Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CFRR

## 2. Definition

Within Code Review & Peer Quality, Critical Findings in Review Rate (CFRR) is used to gauge exposure to adverse outcomes. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Critical or Security Comments / Reviews, expressed in ratio (x:1 or x). It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Software.

## Formula

```
CFRR = Critical or Security Comments / Reviews
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3197 (batch 7)
