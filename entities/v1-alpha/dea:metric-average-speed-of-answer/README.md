# dea:metric-average-speed-of-answer

Candidate Performance Metric record for **Average Speed of Answer** (ASA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-speed-of-answer`
- **Name:** Average Speed of Answer
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ASA

## 2. Definition

A Contact Center indicator, Average Speed of Answer (ASA) quantifies how efficiently resources are converted into outputs. The formula is Total Answer Delay / Calls Answered - reported in seconds. It is applied across virtually every sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Total Answer Delay / Calls Answered
```

## Unit

- **Unit reference:** `dea:unit-seconds`
- **Unit:** seconds
- **Unit label (as published):** seconds

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contact_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 563 (batch 2)
