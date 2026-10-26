# dea:metric-alert-triage-accuracy

Candidate Performance Metric record for **Alert Triage Accuracy** (ATA-SOC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-alert-triage-accuracy`
- **Name:** Alert Triage Accuracy
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ATA-SOC

## 2. Definition

Alert Triage Accuracy (ATA-SOC) measures the quality of outputs and outcomes in the SecOps & Security Operations Center domain. It provides the day-to-day signal that a process is running as designed. Its calculation is Alerts Correctly Categorized on Triage / Sampled, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
ATA-SOC = Alerts Correctly Categorized on Triage / Sampled
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
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** secops_security_operations_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2776 (batch 7)
