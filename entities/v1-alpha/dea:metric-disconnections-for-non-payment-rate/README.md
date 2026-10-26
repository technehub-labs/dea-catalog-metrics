# dea:metric-disconnections-for-non-payment-rate

Candidate Performance Metric record for **Disconnections for Non-Payment Rate** (DNP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-disconnections-for-non-payment-rate`
- **Name:** Disconnections for Non-Payment Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DNP

## 2. Definition

Disconnections for Non-Payment Rate (DNP) captures exposure to adverse outcomes for organizations tracking utilities customer operations. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Disconnections / Customer Accounts, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Utilities.

## 3. Context

Measures the share of customers disconnected for non-payment. It matters because it balances collections rigor against regulatory and humanitarian constraints. Gaming risk includes delaying disconnections past measurement windows or timing them to seasons. Read with Bad Debt Write-Off and Customer Complaint Rate to confirm collection practices are effective and fair.

## Formula

```
Disconnections / Customer Accounts
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 960 (batch 3)
