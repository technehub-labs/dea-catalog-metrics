# dea:metric-patient-fall-rate

Candidate Performance Metric record for **Patient Fall Rate** (PFR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-patient-fall-rate`
- **Name:** Patient Fall Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PFR

## 2. Definition

Patient Fall Rate (PFR) captures exposure to adverse outcomes for organizations tracking healthcare. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Patient Falls / Patient Days x 1,000, expressed in events per thousand or million (scaled). It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Healthcare.

## 3. Context

Measures falls per patient day or per 1,000 patient days. It matters because falls are a leading cause of hospital harm and a direct quality-reporting and liability driver. Coding falls as assisted lowers or incidents as unwitnessed can suppress the true rate. Read with Patient Harm Event trends and staffing ratio data to check whether reported improvement reflects safer care.

## Formula

```
Patient Falls / Patient Days x 1,000
```

## Unit

- **Unit reference:** `dea:unit-events`
- **Unit:** events
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** healthcare
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 475 (batch 1)
