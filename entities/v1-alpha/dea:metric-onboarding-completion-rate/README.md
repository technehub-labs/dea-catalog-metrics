# dea:metric-onboarding-completion-rate

Candidate Performance Metric record for **Onboarding Completion Rate** (OCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-onboarding-completion-rate`
- **Name:** Onboarding Completion Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** OCR

## 2. Definition

Onboarding Completion Rate (OCR) addresses how effectively a process or entity achieves its intended outcome and is a fixture of customer success (b2b saas) reporting. The formula is Accounts Completing Onboarding Milestones / New Accounts - reported in percent (%). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Software & SaaS sector.

## 3. Context

Measures the share of new customers finishing the defined onboarding sequence. It matters because incomplete onboarding predicts early churn in B2B SaaS. Teams can improve it by shortening onboarding so trivially it no longer creates capability. Read with Time to First Value and Activation Rate to confirm completion means genuine readiness, not checkbox progress.

## Formula

```
Accounts Completing Onboarding Milestones / New Accounts
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 583 (batch 2)
