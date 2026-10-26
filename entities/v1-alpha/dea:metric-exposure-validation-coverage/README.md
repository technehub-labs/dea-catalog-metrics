# dea:metric-exposure-validation-coverage

Candidate Performance Metric record for **Exposure Validation Coverage** (EVC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-exposure-validation-coverage`
- **Name:** Exposure Validation Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** EVC

## 2. Definition

Within Vulnerability & Exposure Management, Exposure Validation Coverage (EVC) is used to gauge exposure to adverse outcomes. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Findings Validated as Exploitable / Critical Findings, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Findings Validated as Exploitable / Critical Findings
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** vulnerability_exposure_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2815 (batch 7)
