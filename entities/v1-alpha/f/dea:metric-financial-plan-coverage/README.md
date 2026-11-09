# dea:metric-financial-plan-coverage

Candidate Performance Metric record for **Financial Plan Coverage** (FPC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-financial-plan-coverage`
- **Name:** Financial Plan Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FPC

## 2. Definition

Financial Plan Coverage (FPC) captures how effectively a process or entity achieves its intended outcome for organizations tracking wealth management. It is defined as Clients with Current Written Financial Plan / Clients; the result is stated in percent (%). In Wealth management, it is a recognized element of the standard performance toolkit. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of wealth clients with current financial plans. It matters because planning depth drives client retention and share of assets. Coverage can be met with templated plans never meaningfully discussed. Read with Referral Rate (Wealth) and Net New Assets to confirm plans translate into deeper relationships.

## Formula

```
FPC = Clients with Current Written Financial Plan / Clients
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** wealth_management
- **Sector:** wealth_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1138 (batch 4)
