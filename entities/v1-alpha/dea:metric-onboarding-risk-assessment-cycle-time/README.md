# dea:metric-onboarding-risk-assessment-cycle-time

Candidate Performance Metric record for **Onboarding Risk Assessment Cycle Time** (ORACT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-onboarding-risk-assessment-cycle-time`
- **Name:** Onboarding Risk Assessment Cycle Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ORACT

## 2. Definition

Onboarding Risk Assessment Cycle Time (ORACT) captures how efficiently resources are converted into outputs for organizations tracking third-party risk management. Its calculation is Days from Vendor Request to Risk-Cleared Onboarding, measured in days. It is applied across virtually every sector. Its value drives prioritization and resource reallocation among competing initiatives. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
ORACT = Days from Vendor Request to Risk-Cleared Onboarding
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** risk
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** third_party_risk_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3717 (batch 8)
