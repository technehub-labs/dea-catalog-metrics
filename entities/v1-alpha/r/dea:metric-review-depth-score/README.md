# dea:metric-review-depth-score

Candidate Performance Metric record for **Review Depth Score** (RDS-PR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-review-depth-score`
- **Name:** Review Depth Score
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RDS-PR

## 2. Definition

Within Code Review & Peer Quality, Review Depth Score (RDS-PR) is used to gauge the quality of outputs and outcomes. Its calculation is Composite of Comment Quality, Coverage and Depth Rubric, measured in score (points). It provides the day-to-day signal that a process is running as designed. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Software practice.

## Formula

```
RDS-PR = Composite of Comment Quality, Coverage and Depth Rubric
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3200 (batch 7)
