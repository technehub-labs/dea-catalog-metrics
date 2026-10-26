# dea:metric-billing-accuracy-rate-telecom

Candidate Performance Metric record for **Billing Accuracy Rate (Telecom)** (BART) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-billing-accuracy-rate-telecom`
- **Name:** Billing Accuracy Rate (Telecom)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** BART

## 2. Definition

A Telecom Customer Experience & Billing indicator, Billing Accuracy Rate (Telecom) (BART) quantifies the quality of outputs and outcomes. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Bills Issued without Dispute or Correction / Bills Issued; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. In Telecommunications, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the share of invoices issued without error, the most visible trust test in an industry with notoriously complex rating plans. Inaccurate bills drive calls, disputes, churn, and regulatory exposure in equal measure, so small percentage gains carry outsized financial and reputational value. The gaming risk is defining accuracy as what-the-system-said rather than what-the-customer-owed, which hides rating and provisioning errors upstream. Read with average revenue leakage (Telecom) and billing complaint volumes.

## Formula

```
Bills Issued without Dispute or Correction / Bills Issued
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** telecom_customer_experience_billing
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1266 (batch 5)
