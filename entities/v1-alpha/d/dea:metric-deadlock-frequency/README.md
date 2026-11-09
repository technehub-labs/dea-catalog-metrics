# dea:metric-deadlock-frequency

Candidate Performance Metric record for **Deadlock Frequency** (DLF-DB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-deadlock-frequency`
- **Name:** Deadlock Frequency
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DLF-DB

## 2. Definition

A Database & Data Platform Operations indicator, Deadlock Frequency (DLF-DB) quantifies the quality of outputs and outcomes. The formula is Deadlocks per Period - reported in count (items per period). It is a standard measure in the Software sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
DLF-DB = Deadlocks per Period
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** database_data_platform_operations
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3235 (batch 7)
