# dea:metric-cash-ratio-deep-dive

Candidate Performance Metric record for **Cash Ratio (Deep Dive)** (CashRD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cash-ratio-deep-dive`
- **Name:** Cash Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CashRD

## 2. Definition

Cash Ratio (Deep Dive) (CashRD) measures exposure to adverse outcomes in the Financial Statement Analysis Ratios (Deep Dive) domain. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Cash and Equivalents / Current Liabilities - reported in ratio (x:1 or x). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures cash and near-cash against current liabilities. It is the most conservative liquidity test and the one that matters when credit vanishes. Persistently high ratios can signal idle capital rather than prudence. Read with quick ratio (Deep Dive) and cash buffer coverage.

## Formula

```
Cash and Equivalents / Current Liabilities
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** financial_statement_analysis_ratios_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4017 (batch 9)
