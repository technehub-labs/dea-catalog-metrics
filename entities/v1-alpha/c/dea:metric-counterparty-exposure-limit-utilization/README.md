# dea:metric-counterparty-exposure-limit-utilization

Candidate Performance Metric record for **Counterparty Exposure Limit Utilization** (CELU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-counterparty-exposure-limit-utilization`
- **Name:** Counterparty Exposure Limit Utilization
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CELU

## 2. Definition

Counterparty Exposure Limit Utilization (CELU) measures exposure to adverse outcomes in the Treasury & Cash Management domain. It is computed as Exposure to Counterparty / Approved Limit, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures current counterparty exposure relative to approved credit limits. It matters because concentrated, unmanaged exposure is the classic path to sudden credit losses. Gaming risk includes netting agreements applied loosely or exposures parked in affiliates under different limits. Read with Counterparty Credit Rating and Concentration metrics to check whether headroom reflects real risk control.

## Formula

```
CELU = Exposure to Counterparty / Approved Limit
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** treasury_cash_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 597 (batch 2)
