# dea:metric-quality-monitoring-score

Candidate Performance Metric record for **Quality Monitoring Score** (QMS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-quality-monitoring-score`
- **Name:** Quality Monitoring Score
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** QMS

## 2. Definition

Quality Monitoring Score (QMS) addresses the quality of outputs and outcomes and is a fixture of contact center reporting. The formula is Average QA Evaluation Score of Recorded Interactions - reported in score (points). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Average QA Evaluation Score of Recorded Interactions
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contact_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 575 (batch 2)
