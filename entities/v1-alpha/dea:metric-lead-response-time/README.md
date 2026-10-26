# dea:metric-lead-response-time

Candidate Performance Metric record for **Lead Response Time** (LRT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-lead-response-time`
- **Name:** Lead Response Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** LRT

## 2. Definition

Lead Response Time (LRT) addresses how efficiently resources are converted into outputs and is a fixture of sales reporting. It is defined as Average Time from Lead Arrival to First Response; the result is stated in minutes. It is applied across virtually every sector. It is a working-level control: thresholds trigger immediate operational response. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Average Time from Lead Arrival to First Response
```

## Unit

- **Unit reference:** `dea:unit-minutes`
- **Unit:** minutes
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sales

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 95 (batch 1)
