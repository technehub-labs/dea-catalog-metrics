# dea:metric-contract-end-churn-risk-conversion

Candidate Performance Metric record for **Contract End Churn Risk Conversion** (CERC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-contract-end-churn-risk-conversion`
- **Name:** Contract End Churn Risk Conversion
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CERC

## 2. Definition

A Telecom Customer Experience & Billing indicator, Contract End Churn Risk Conversion (CERC) quantifies the retention of customers, users, or assets over time. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as At-Risk Customers Retained at Contract End / At-Risk Customers; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. In Telecommunications, it is a recognized element of the standard performance toolkit.

## 3. Context

Tracks how many customers identified as at-risk at contract expiry are actually saved - via offer, upgrade, or engagement - versus how many lapse. It converts churn management from retrospective reporting into forward intervention yield. The gaming risks are retention offers that merely buy a quarter at punishing margin, and risk models tuned to flag only easy saves. Track the post-save twelve-month survival of saved customers, not just the save itself. Read with churn model recall and win-back economics.

## Formula

```
At-Risk Customers Retained at Contract End / At-Risk Customers
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** retention
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1277 (batch 5)
