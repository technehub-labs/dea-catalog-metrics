# dea:metric-author-response-time-in-review

Candidate Performance Metric record for **Author Response Time in Review** (ART-PR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-author-response-time-in-review`
- **Name:** Author Response Time in Review
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ART-PR

## 2. Definition

Author Response Time in Review (ART-PR) measures how efficiently resources are converted into outputs in the Code Review & Peer Quality domain. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Median Hours for Author to Address Comments, expressed in hours. It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Software.

## Formula

```
ART-PR = Median Hours for Author to Address Comments
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3204 (batch 7)
