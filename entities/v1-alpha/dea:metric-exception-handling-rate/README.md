# dea:metric-exception-handling-rate

Candidate Performance Metric record for **Exception Handling Rate** (EHR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-exception-handling-rate`
- **Name:** Exception Handling Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** EHR

## 2. Definition

A Automation & Robotic Process Automation indicator, Exception Handling Rate (EHR) quantifies the quality of outputs and outcomes. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Bot Executions Routed to Manual Handling / Bot Executions, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Bot Executions Routed to Manual Handling / Bot Executions
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** automation_robotic_process_automation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1325 (batch 5)
