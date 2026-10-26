# dea:metric-first-bill-right-rate

Candidate Performance Metric record for **First Bill Right Rate** (FBRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-first-bill-right-rate`
- **Name:** First Bill Right Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FBRR

## 2. Definition

A Telecom Customer Experience & Billing indicator, First Bill Right Rate (FBRR) quantifies the quality of outputs and outcomes. Its calculation is First Bills without Error / New Customer Bills, measured in percent (%). It originates from and is most used in Telecommunications practice. Its value drives prioritization and resource reallocation among competing initiatives. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of first bills issued correctly without adjustment. It matters because the first bill is the trust-establishing moment of the customer relationship. Gaming risk includes issuing pro-forma placeholder bills that are corrected later. Read with Dispute Rate (Billing) and Call Driver analysis to confirm first bills are truly right.

## Formula

```
First Bills without Error / New Customer Bills
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** telecom_customer_experience_billing
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1268 (batch 5)
