# dea:metric-commit-to-build-latency

Candidate Performance Metric record for **Commit-to-Build Latency** (CTBL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-commit-to-build-latency`
- **Name:** Commit-to-Build Latency
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CTBL

## 2. Definition

Commit-to-Build Latency (CTBL) measures how efficiently resources are converted into outputs in the Continuous Integration domain. It is defined as Minutes from Commit to Build Start; the result is stated in minutes. It is a working-level control: thresholds trigger immediate operational response. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Minutes from Commit to Build Start
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
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** continuous_integration

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2663 (batch 7)
