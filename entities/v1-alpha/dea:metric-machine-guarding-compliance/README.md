# dea:metric-machine-guarding-compliance

Candidate Performance Metric record for **Machine Guarding Compliance** (MGC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-machine-guarding-compliance`
- **Name:** Machine Guarding Compliance
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MGC

## 2. Definition

Machine Guarding Compliance (MGC) captures conformance to standards, plans, or obligations for organizations tracking health & safety. Its calculation is Guarded Hazards / Identified Machine Hazards, measured in percent (%). It provides the day-to-day signal that a process is running as designed. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Guarded Hazards / Identified Machine Hazards
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** health_safety

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 409 (batch 1)
