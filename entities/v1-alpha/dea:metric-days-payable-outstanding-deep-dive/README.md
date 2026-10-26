# dea:metric-days-payable-outstanding-deep-dive

Candidate Performance Metric record for **Days Payable Outstanding (Deep Dive)** (DPODD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-days-payable-outstanding-deep-dive`
- **Name:** Days Payable Outstanding (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DPODD

## 2. Definition

Days Payable Outstanding (Deep Dive) (DPODD) measures how efficiently resources are converted into outputs in the Accounts Payable & Receivable Operations (Deep Dive) domain. It is defined as Average Days from Invoice to Payment; the result is stated in days. It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures the average time taken to pay suppliers. DPO is working capital, but also supply-chain health: stretched payment erodes supplier pricing and reliability. Payment terms extracted as leverage reappear as supplier cost. Read with days sales outstanding (Deep Dive) and cash conversion cycle (Working Capital).

## Formula

```
Average Days from Invoice to Payment
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** accounts_payable_receivable_operations_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3801 (batch 8)
