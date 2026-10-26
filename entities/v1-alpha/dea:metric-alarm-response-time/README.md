# dea:metric-alarm-response-time

Candidate Performance Metric record for **Alarm Response Time** (ALRT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-alarm-response-time`
- **Name:** Alarm Response Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ALRT

## 2. Definition

Alarm Response Time (ALRT) captures how efficiently resources are converted into outputs for organizations tracking physical security operations. Its calculation is Minutes from Alarm to Security Response on Scene, measured in minutes. It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Minutes from Alarm to Security Response on Scene
```

## Unit

- **Unit reference:** `dea:unit-minutes`
- **Unit:** minutes
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** governance
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** physical_security_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1204 (batch 4)
