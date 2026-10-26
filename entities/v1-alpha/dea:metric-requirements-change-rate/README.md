# dea:metric-requirements-change-rate

Candidate Performance Metric record for **Requirements Change Rate** (RCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-requirements-change-rate`
- **Name:** Requirements Change Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RCR

## 2. Definition

Requirements Change Rate (RCR) captures exposure to adverse outcomes for organizations tracking project management. It is defined as Changed Requirements / Baseline Requirements; the result is stated in percent (%). It is applied across virtually every sector. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the rate of change to requirements after baseline approval. It matters because churn after baseline is the leading cause of scope creep and delivery failure. It can be gamed by deferring change requests until after milestones, so churn hides in a backlog. Read with Baseline Scope Stability and Cost Performance Index to see whether change is being managed or just delayed.

## Formula

```
RCR = Changed Requirements / Baseline Requirements
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** transformation
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** project_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 354 (batch 1)
