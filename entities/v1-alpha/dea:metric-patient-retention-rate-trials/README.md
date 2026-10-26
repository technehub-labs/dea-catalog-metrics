# dea:metric-patient-retention-rate-trials

Candidate Performance Metric record for **Patient Retention Rate (Trials)** (PRR-T) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-patient-retention-rate-trials`
- **Name:** Patient Retention Rate (Trials)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PRR-T

## 2. Definition

Patient Retention Rate (Trials) (PRR-T) addresses the retention of customers, users, or assets over time and is a fixture of pharma r&d & clinical trials reporting. The formula is Subjects Completing Study / Subjects Enrolled - reported in percent (%). It is a standard measure in the Pharmaceuticals sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
PRR-T = Subjects Completing Study / Subjects Enrolled
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** retention
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** pharma_r_d_clinical_trials
- **Sector:** pharmaceuticals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1609 (batch 6)
