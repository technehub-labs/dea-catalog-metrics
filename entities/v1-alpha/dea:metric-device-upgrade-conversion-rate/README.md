# dea:metric-device-upgrade-conversion-rate

Candidate Performance Metric record for **Device Upgrade Conversion Rate** (DUCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-device-upgrade-conversion-rate`
- **Name:** Device Upgrade Conversion Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DUCR

## 2. Definition

Device Upgrade Conversion Rate (DUCR) captures growth over time for organizations tracking telecom customer experience & billing. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Upgrades Completed / Upgrade-Eligible Customers; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. In Telecommunications, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the share of eligible customers upgrading devices. It matters because upgrades drive handset revenue, attachment, and re-contracting moments. Pushing upgrades to unsuitable tariffs buys conversion at churn-risk cost. Read with Post-Upgrade Churn and Average Revenue per User trends to confirm upgrade conversions are healthy.

## Formula

```
Upgrades Completed / Upgrade-Eligible Customers
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** telecom_customer_experience_billing
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1276 (batch 5)
