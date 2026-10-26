# dea:metric-problem-record-backlog-age

Candidate Performance Metric record for **Problem Record Backlog Age** (PRBA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-problem-record-backlog-age`
- **Name:** Problem Record Backlog Age
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PRBA

## 2. Definition

Problem Record Backlog Age (PRBA) captures how efficiently resources are converted into outputs for organizations tracking it incident & major problem management. It is computed as Open Problems beyond 90 Days / Open Problems, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Open Problems beyond 90 Days / Open Problems
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** it_incident_major_problem_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2894 (batch 7)
