# dea:metric-app-release-cadence

Candidate Performance Metric record for **App Release Cadence** (ARC-MOB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-app-release-cadence`
- **Name:** App Release Cadence
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ARC-MOB

## 2. Definition

App Release Cadence (ARC-MOB) measures how efficiently resources are converted into outputs in the Mobile & Client Development domain. Its calculation is Production App Releases per Month, measured in times per period. It originates from and is most used in Software practice. It provides the day-to-day signal that a process is running as designed. Values outside the intended band, on either side, warrant investigation.

## Formula

```
ARC-MOB = Production App Releases per Month
```

## Unit

- **Unit reference:** `dea:unit-times`
- **Unit:** times
- **Unit label (as published):** times per period

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** mobile_client_development
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3249 (batch 7)
