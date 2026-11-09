# dea:metric-referral-loop-closure-rate

Candidate Performance Metric record for **Referral Loop Closure Rate** (RLCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-referral-loop-closure-rate`
- **Name:** Referral Loop Closure Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RLCR

## 2. Definition

Referral Loop Closure Rate (RLCR) measures the quality of outputs and outcomes in the Medical Practice & Clinical Operations domain. It is computed as Referrals with Specialist Report Returned / Referrals, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Healthcare.

## Formula

```
RLCR = Referrals with Specialist Report Returned / Referrals
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** medical_practice_clinical_operations
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1634 (batch 6)
