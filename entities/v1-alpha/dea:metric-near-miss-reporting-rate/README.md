# dea:metric-near-miss-reporting-rate

Candidate Performance Metric record for **Near Miss Reporting Rate** (NMRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-near-miss-reporting-rate`
- **Name:** Near Miss Reporting Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** NMRR

## 2. Definition

Within Health & Safety, Near Miss Reporting Rate (NMRR) is used to gauge exposure to adverse outcomes. It is computed as Near Misses Reported per 100 Employees, expressed in ratio (x:1 or x). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the frequency of reported near-miss incidents per workforce or hours worked. It matters because near misses are free lessons; a rising rate often signals improving safety culture, not danger. Misreading the direction is the classic trap: falling reports can mean fear, not safety. Read with Recordable Incident Rate and safety culture survey results to interpret the trend correctly.

## Formula

```
Near Misses Reported per 100 Employees
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** health_safety

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 400 (batch 1)
