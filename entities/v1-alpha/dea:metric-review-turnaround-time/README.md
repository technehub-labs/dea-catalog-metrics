# dea:metric-review-turnaround-time

Candidate Performance Metric record for **Review Turnaround Time** (RTT-PR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-review-turnaround-time`
- **Name:** Review Turnaround Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RTT-PR

## 2. Definition

Review Turnaround Time (RTT-PR) measures how efficiently resources are converted into outputs in the Code Review & Peer Quality domain. The formula is Hours from Review Request to First Response - reported in hours. It is a standard measure in the Software sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Hours from Review Request to First Response
```

## Unit

- **Unit reference:** `dea:unit-hours`
- **Unit:** hours
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3187 (batch 7)
