# dea:metric-emergency-change-rate

Candidate Performance Metric record for **Emergency Change Rate** (ECR-T) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-emergency-change-rate`
- **Name:** Emergency Change Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ECR-T

## 2. Definition

A IT Service Management indicator, Emergency Change Rate (ECR-T) quantifies exposure to adverse outcomes. Its calculation is Emergency Changes / Total Changes, measured in percent (%). Its value drives prioritization and resource reallocation among competing initiatives. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of changes executed through emergency channels. It matters because emergency changes bypass review and are a leading outage driver. Teams can normalize emergency status to skip paperwork, inflating the metric it should reduce. Read with Change Success Rate and Problem Recurrence Rate to see whether the emergency lane is shrinking or being disguised.

## Formula

```
ECR-T = Emergency Changes / Total Changes
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
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** it_service_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 306 (batch 1)
