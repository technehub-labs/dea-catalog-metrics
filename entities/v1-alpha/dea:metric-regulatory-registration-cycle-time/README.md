# dea:metric-regulatory-registration-cycle-time

Candidate Performance Metric record for **Regulatory Registration Cycle Time** (RRCT-C) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-regulatory-registration-cycle-time`
- **Name:** Regulatory Registration Cycle Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RRCT-C

## 2. Definition

Regulatory Registration Cycle Time (RRCT-C) captures how efficiently resources are converted into outputs for organizations tracking chemicals. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Days from Registration Dossier Submission to Approval, expressed in days. It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Chemicals.

## 3. Context

Measures time to complete product registrations with authorities. It matters because registration gates market access for chemical products. It can be gamed by excluding time spent responding to authority questions as external delay. Read with First-Pass Approval Rate and registration cost to confirm speed reflects quality dossiers.

## Formula

```
Days from Registration Dossier Submission to Approval
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** chemicals
- **Sector:** chemicals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 902 (batch 3)
