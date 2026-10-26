# dea:metric-bank-account-rationalization

Candidate Performance Metric record for **Bank Account Rationalization** (BAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-bank-account-rationalization`
- **Name:** Bank Account Rationalization
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** BAR

## 2. Definition

A Treasury & Cash Management indicator, Bank Account Rationalization (BAR) quantifies how efficiently resources are converted into outputs. The formula is Active Bank Accounts / Total Bank Accounts Held - reported in percent (%). It is applied across virtually every sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures progress consolidating bank accounts toward the target structure. It matters because every redundant account carries fees, KYC overhead, and cash fragmentation. Rationalization can stall by reclassifying zombie accounts as strategically retained. Read with Cash Visibility coverage and bank fee spend to confirm consolidation delivers its promised treasury benefits.

## Formula

```
Active Bank Accounts / Total Bank Accounts Held
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** treasury_cash_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 598 (batch 2)
