# dea:metric-debt-service-coverage-ratio-borrowers

Candidate Performance Metric record for **Debt Service Coverage Ratio (Borrowers)** (DSCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-debt-service-coverage-ratio-borrowers`
- **Name:** Debt Service Coverage Ratio (Borrowers)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DSCR

## 2. Definition

A Retail Banking & Lending indicator, Debt Service Coverage Ratio (Borrowers) (DSCR) quantifies exposure to adverse outcomes. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Net Operating Income / Debt Service Obligations - reported in ratio (x:1 or x). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Banking sector.

## 3. Context

Measures borrower cash flow relative to scheduled debt service. It matters because it is the primary repayment-capacity read behind lending decisions. Borrower-provided cash flow can be inflated with aggressive addbacks. Read with Payment Delinquency trends and Stress-Tested DSCR to confirm coverage holds under realistic assumptions.

## Formula

```
Net Operating Income / Debt Service Obligations
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** retail_banking_lending
- **Sector:** banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 844 (batch 3)
