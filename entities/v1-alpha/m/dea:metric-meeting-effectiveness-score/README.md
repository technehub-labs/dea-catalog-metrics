# dea:metric-meeting-effectiveness-score

Candidate Performance Metric record for **Meeting Effectiveness Score** (MES) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-meeting-effectiveness-score`
- **Name:** Meeting Effectiveness Score
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MES

## 2. Definition

Meeting Effectiveness Score (MES) addresses the engagement or satisfaction of the people involved and is a fixture of operating model & decision effectiveness reporting. The formula is Average Post-Meeting Effectiveness Rating - reported in score (points). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
MES = Average Post-Meeting Effectiveness Rating
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** organization
- **Purpose classification:** engagement
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** operating_model_decision_effectiveness

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1303 (batch 5)
