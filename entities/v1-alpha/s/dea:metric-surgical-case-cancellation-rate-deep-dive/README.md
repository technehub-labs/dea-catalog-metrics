# dea:metric-surgical-case-cancellation-rate-deep-dive

Candidate Performance Metric record for **Surgical Case Cancellation Rate (Deep Dive)** (SCCR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-surgical-case-cancellation-rate-deep-dive`
- **Name:** Surgical Case Cancellation Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SCCR-D

## 2. Definition

Surgical Case Cancellation Rate (Deep Dive) (SCCR-D) addresses how efficiently resources are converted into outputs and is a fixture of medical practice & clinical operations reporting. It is computed as Cases Cancelled Day of Surgery / Cases Scheduled, expressed in percent (%). Its use is concentrated in Healthcare. It is reviewed at cadence by planning owners to correct course before issues become strategic. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
SCCR-D = Cases Cancelled Day of Surgery / Cases Scheduled
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** medical_practice_clinical_operations
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1644 (batch 6)
