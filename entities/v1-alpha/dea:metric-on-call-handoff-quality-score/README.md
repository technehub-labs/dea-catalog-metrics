# dea:metric-on-call-handoff-quality-score

Candidate Performance Metric record for **On-Call Handoff Quality Score** (OCHQS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-on-call-handoff-quality-score`
- **Name:** On-Call Handoff Quality Score
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** OCHQS

## 2. Definition

On-Call Handoff Quality Score (OCHQS) addresses the quality of outputs and outcomes and is a fixture of observability & site reliability engineering reporting. Its calculation is Handoff Survey Completeness Score, measured in score (points). It is applied across virtually every sector. It provides the day-to-day signal that a process is running as designed. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
OCHQS = Handoff Survey Completeness Score
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** observability_site_reliability_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2871 (batch 7)
