# dea:metric-guaranteed-service-level-payments

Candidate Performance Metric record for **Guaranteed Service Level Payments** (GSLP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-guaranteed-service-level-payments`
- **Name:** Guaranteed Service Level Payments
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** GSLP

## 2. Definition

Within Utilities Customer Operations, Guaranteed Service Level Payments (GSLP) is used to gauge conformance to standards, plans, or obligations. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Service Standard Payments Issued / Customers; the result is stated in ratio (x:1 or x). It should be driven down, since lower readings signal healthier performance. In Utilities, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the value of penalty payments made for missing contracted service levels in utility operations. It matters because these payments are the direct financial cost of reliability failure. Teams can reduce them by negotiating weaker service level definitions rather than improving performance. Read with Customer Average Interruption Duration Index and Unplanned Outage Rate to confirm payment reductions reflect better service.

## Formula

```
Service Standard Payments Issued / Customers
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** customer
- **Purpose classification:** compliance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 963 (batch 3)
