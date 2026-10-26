# dea:metric-noc-mean-time-to-acknowledge

Candidate Performance Metric record for **NOC Mean Time to Acknowledge** (NOMTA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-noc-mean-time-to-acknowledge`
- **Name:** NOC Mean Time to Acknowledge
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** NOMTA

## 2. Definition

NOC Mean Time to Acknowledge (NOMTA) measures how efficiently resources are converted into outputs in the Network Operations Center (Deep Dive) domain. Its calculation is Minutes from Alert to NOC Acknowledgment, measured in minutes. It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Minutes from Alert to NOC Acknowledgment
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** network_operations_center_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2838 (batch 7)
