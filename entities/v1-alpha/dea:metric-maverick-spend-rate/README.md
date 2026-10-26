# dea:metric-maverick-spend-rate

Candidate Performance Metric record for **Maverick Spend Rate** (MSR-P) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-maverick-spend-rate`
- **Name:** Maverick Spend Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MSR-P

## 2. Definition

Maverick Spend Rate (MSR-P) measures conformance to standards, plans, or obligations in the Procurement domain. It is defined as Off-Contract Spend / Total Spend; the result is stated in percent (%). It is applied across virtually every sector. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the share of spend made outside approved contracts and channels. It matters because off-channel buying destroys negotiated leverage, compliance, and data quality. Teams can shrink it cosmetically by reclassifying exceptions as approved emergencies. Read with Contract Compliance Rate and Purchase Price Variance to confirm rising control is not just definitional cleanup.

## Formula

```
Off-Contract Spend / Total Spend
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** procurement

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 229 (batch 1)
