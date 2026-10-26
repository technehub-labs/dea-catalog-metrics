# dea:metric-code-review-coverage-deep-dive

Candidate Performance Metric record for **Code Review Coverage (Deep Dive)** (CRC-PR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-code-review-coverage-deep-dive`
- **Name:** Code Review Coverage (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CRC-PR

## 2. Definition

Code Review Coverage (Deep Dive) (CRC-PR) measures the quality of outputs and outcomes in the Code Review & Peer Quality domain. It is computed as Changes Reviewed before Merge / Total Changes, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Software.

## Formula

```
CRC-PR = Changes Reviewed before Merge / Total Changes
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** code_review_peer_quality
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3186 (batch 7)
