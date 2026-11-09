# dea:metric-machine-vision-first-pass-inspection-rate

Candidate Performance Metric record for **Machine Vision First-Pass Inspection Rate** (MVFI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-machine-vision-first-pass-inspection-rate`
- **Name:** Machine Vision First-Pass Inspection Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MVFI

## 2. Definition

A Industrial Automation & Robotics indicator, Machine Vision First-Pass Inspection Rate (MVFI) quantifies the quality of outputs and outcomes. Its calculation is Inspections Correctly Classified First Time / Inspections, measured in percent (%). It provides the day-to-day signal that a process is running as designed. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Manufacturing practice.

## Formula

```
MVFI = Inspections Correctly Classified First Time / Inspections
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** industrial_automation_robotics
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1339 (batch 5)
