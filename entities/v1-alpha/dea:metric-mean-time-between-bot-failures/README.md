# dea:metric-mean-time-between-bot-failures

Candidate Performance Metric record for **Mean Time between Bot Failures** (MTBBF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mean-time-between-bot-failures`
- **Name:** Mean Time between Bot Failures
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MTBBF

## 2. Definition

A Automation & Robotic Process Automation indicator, Mean Time between Bot Failures (MTBBF) quantifies exposure to adverse outcomes. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Total Bot Operating Time / Bot Failures, expressed in hours. Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Total Bot Operating Time / Bot Failures
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** automation_robotic_process_automation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1328 (batch 5)
