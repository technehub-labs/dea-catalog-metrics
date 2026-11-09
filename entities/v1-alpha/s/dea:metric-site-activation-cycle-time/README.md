# dea:metric-site-activation-cycle-time

Candidate Performance Metric record for **Site Activation Cycle Time** (SACT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-site-activation-cycle-time`
- **Name:** Site Activation Cycle Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SACT

## 2. Definition

Site Activation Cycle Time (SACT) addresses how efficiently resources are converted into outputs and is a fixture of pharma r&d & clinical trials reporting. It is defined as Days from Site Selection to Site Activation; the result is stated in days. In Pharmaceuticals, it is a recognized element of the standard performance toolkit. It is a working-level control: thresholds trigger immediate operational response. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
SACT = Days from Site Selection to Site Activation
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** pharma_r_d_clinical_trials
- **Sector:** pharmaceuticals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1617 (batch 6)
