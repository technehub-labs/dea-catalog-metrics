# dea:metric-know-your-customer-onboarding-time

Candidate Performance Metric record for **Know-Your-Customer Onboarding Time** (KYCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-know-your-customer-onboarding-time`
- **Name:** Know-Your-Customer Onboarding Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** KYCT

## 2. Definition

Know-Your-Customer Onboarding Time (KYCT) measures how efficiently resources are converted into outputs in the Payments & Fintech domain. It is defined as Days from Application to Approval; the result is stated in days. In Payments & fintech, it is a recognized element of the standard performance toolkit. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures days from application to fully KYC-verified onboarding. It matters because every verification day loses impatient applicants to competitors. It can be gamed by loosening verification thresholds, trading speed for AML risk. Read with KYC Remediation backlog and False Positive Rate to confirm speed does not come from softer checks.

## Formula

```
Days from Application to Approval
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** payments_fintech
- **Sector:** payments_fintech

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 785 (batch 2)
