# dea:metric-corrective-and-preventive-action-closure-rate

Candidate Performance Metric record for **Corrective and Preventive Action Closure Rate** (CAPA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-corrective-and-preventive-action-closure-rate`
- **Name:** Corrective and Preventive Action Closure Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CAPA

## 2. Definition

Within Medical Devices, Corrective and Preventive Action Closure Rate (CAPA) is used to gauge conformance to standards, plans, or obligations. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as CAPAs Closed on Time / CAPAs Opened, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Medical devices.

## 3. Context

Measures the share of CAPAs closed on schedule in medical device quality systems. It matters because open CAPAs are regulatory findings waiting to happen and unresolved patient risk. Closures can be declared when documentation is complete while the fix is not deployed in production. Read with CAPA Effectiveness checks and external audit findings to confirm closures are verified.

## Formula

```
CAPAs Closed on Time / CAPAs Opened
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** medical_devices
- **Sector:** medical_devices

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 757 (batch 2)
