# dea:metric-threshold-alert-rate

Candidate Performance Metric record for **Threshold Alert Rate** (THAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-threshold-alert-rate`
- **Name:** Threshold Alert Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** THAR

## 2. Definition

Threshold Alert Rate (THAR) captures how efficiently resources are converted into outputs for organizations tracking statistical model performance diagnostics. It provides the day-to-day signal that a process is running as designed. Its calculation is Scored Cases Requiring Manual Review at Threshold / Cases, measured in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. It originates from and is most used in Software practice.

## Formula

```
THAR = Scored Cases Requiring Manual Review at Threshold / Cases
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** statistical_model_performance_diagnostics
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4072 (batch 9)
