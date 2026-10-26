# dea:metric-estimated-bill-rate

Candidate Performance Metric record for **Estimated Bill Rate** (EBR-U) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-estimated-bill-rate`
- **Name:** Estimated Bill Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** EBR-U

## 2. Definition

Estimated Bill Rate (EBR-U) captures the quality of outputs and outcomes for organizations tracking utilities customer operations. Its calculation is Estimated Bills / Total Bills Issued, measured in percent (%). It originates from and is most used in Utilities practice. Its value drives prioritization and resource reallocation among competing initiatives. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the share of utility customers billed on estimated rather than actual meter reads. It matters because high estimation correlates with billing complaints, rework, and revenue error. Estimation can look fine statistically while particular customers get punishing true-up bills. Read with Billing Complaint Rate and Meter Read Success Rate to confirm estimation is controlled.

## Formula

```
Estimated Bills / Total Bills Issued
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** utilities_customer_operations
- **Sector:** utilities

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 958 (batch 3)
