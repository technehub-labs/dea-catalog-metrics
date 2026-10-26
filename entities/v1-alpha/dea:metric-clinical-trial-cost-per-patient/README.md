# dea:metric-clinical-trial-cost-per-patient

Candidate Performance Metric record for **Clinical Trial Cost per Patient** (CTCP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-clinical-trial-cost-per-patient`
- **Name:** Clinical Trial Cost per Patient
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CTCP

## 2. Definition

Within Pharma R&D & Clinical Trials, Clinical Trial Cost per Patient (CTCP) is used to gauge how efficiently resources are converted into outputs. It is computed as Trial Costs / Patients Enrolled, expressed in currency value. Its use is concentrated in Pharmaceuticals. It is reviewed at cadence by planning owners to correct course before issues become strategic. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
CTCP = Trial Costs / Patients Enrolled
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** pharma_r_d_clinical_trials
- **Sector:** pharmaceuticals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1616 (batch 6)
