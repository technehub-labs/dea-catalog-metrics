# dea:metric-human-in-the-loop-intervention-rate

Candidate Performance Metric record for **Human-in-the-Loop Intervention Rate** (HITL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-human-in-the-loop-intervention-rate`
- **Name:** Human-in-the-Loop Intervention Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** HITL

## 2. Definition

Human-in-the-Loop Intervention Rate (HITL) measures exposure to adverse outcomes in the Automation & Robotic Process Automation domain. Its calculation is Cases Requiring Human Override / Automated Cases, measured in percent (%). It is applied across virtually every sector. Its value drives prioritization and resource reallocation among competing initiatives. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures how often automated processes require human intervention. It matters because intervention rate is the honest measure of true automation maturity. Exception handling can be pushed to untracked back-office queues, hiding the rate. Read with Bot Utilization Rate and end-to-end Straight-Through Processing Rate to confirm automation is real.

## Formula

```
HITL = Cases Requiring Human Override / Automated Cases
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** automation_robotic_process_automation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1332 (batch 5)
