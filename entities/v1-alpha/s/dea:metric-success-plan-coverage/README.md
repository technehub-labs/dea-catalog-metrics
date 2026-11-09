# dea:metric-success-plan-coverage

Candidate Performance Metric record for **Success Plan Coverage** (SPC-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-success-plan-coverage`
- **Name:** Success Plan Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SPC-S

## 2. Definition

Success Plan Coverage (SPC-S) addresses how effectively a process or entity achieves its intended outcome and is a fixture of customer success (b2b saas) reporting. It is computed as Accounts with Agreed Success Plan / Total Accounts, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Software & SaaS.

## 3. Context

Measures the share of customers with a documented, current customer success plan. It matters because explicit goals are how account teams align value delivery to renewal. Coverage can be gamed with boilerplate plans copied across accounts without engagement. Read with Net Revenue Retention and Onboarding Completion Rate to confirm plans drive outcomes rather than paperwork.

## Formula

```
SPC-S = Accounts with Agreed Success Plan / Total Accounts
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** customer_success_b2b_saas
- **Sector:** software_saas

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 588 (batch 2)
