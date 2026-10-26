# dea:metric-value-leakage-from-missed-renewals

Candidate Performance Metric record for **Value Leakage from Missed Renewals** (VLMR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-value-leakage-from-missed-renewals`
- **Name:** Value Leakage from Missed Renewals
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** VLMR

## 2. Definition

Value Leakage from Missed Renewals (VLMR) measures the economic value created or preserved in the Contract Lifecycle Management domain. Its calculation is Spend on Unwanted Auto-Renewals in Period, measured in currency value. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the value lost to auto-renewals, unnoticed expirations, and unexercised rights. Contract value is created at negotiation and destroyed at administration. Leakage measured only on headline contracts understates the long tail. Read with renewal pipeline coverage and contract compliance rate.

## Formula

```
Spend on Unwanted Auto-Renewals in Period
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** organization
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contract_lifecycle_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3701 (batch 8)
