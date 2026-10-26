# dea:metric-activation-rate

Candidate Performance Metric record for **Activation Rate** (ACT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-activation-rate`
- **Name:** Activation Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ACT

## 2. Definition

Activation Rate (ACT) captures how effectively a process or entity achieves its intended outcome for organizations tracking product management. It is computed as Users Reaching Activation Milestone / New Users, expressed in percent (%). It is applied across virtually every sector. It is reviewed at cadence by planning owners to correct course before issues become strategic. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of new signups reaching the defined activation milestone. It matters because activation is the strongest early predictor of retention and expansion. Gaming risk includes lowering the activation bar until it is trivially reachable. Read with Onboarding Completion Rate and Time to Value to confirm activation definitions track genuine realized value.

## Formula

```
Users Reaching Activation Milestone / New Users
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** product_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 557 (batch 1)
