# dea:metric-backup-restore-test-pass-rate

Candidate Performance Metric record for **Backup Restore Test Pass Rate** (BRT-PR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-backup-restore-test-pass-rate`
- **Name:** Backup Restore Test Pass Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** BRT-PR

## 2. Definition

Backup Restore Test Pass Rate (BRT-PR) addresses exposure to adverse outcomes and is a fixture of database & data platform operations reporting. It provides the day-to-day signal that a process is running as designed. Its calculation is Restore Tests Passed / Restore Tests Executed, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Software practice.

## Formula

```
Restore Tests Passed / Restore Tests Executed
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** database_data_platform_operations
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3230 (batch 7)
