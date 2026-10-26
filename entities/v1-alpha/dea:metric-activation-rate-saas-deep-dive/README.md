# dea:metric-activation-rate-saas-deep-dive

Candidate Performance Metric record for **Activation Rate (SaaS Deep Dive)** (ACT-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-activation-rate-saas-deep-dive`
- **Name:** Activation Rate (SaaS Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ACT-D

## 2. Definition

Activation Rate (SaaS Deep Dive) (ACT-D) measures growth over time in the Software Product Operations (Deep Dive) domain. The formula is Accounts Reaching Activation / Signups - reported in percent (%). It is a standard measure in the Technology sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of new accounts reaching defined activation milestones (invited team, core workflow completion). Activation is the product-market confirmation of each sale, and unactivated accounts churn at multiples of activated ones regardless of sales claims. Activation definitions must be tailored by use case, since one milestone cannot fit horizontal products. Read with time to value - onboarding (SaaS Deep Dive) and trial-to-paid conversion (Deep Dive).

## Formula

```
Accounts Reaching Activation / Signups
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** software_product_operations_deep_dive
- **Sector:** technology

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2156 (batch 6)
