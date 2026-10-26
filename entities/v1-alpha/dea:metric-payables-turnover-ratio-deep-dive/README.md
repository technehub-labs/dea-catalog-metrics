# dea:metric-payables-turnover-ratio-deep-dive

Candidate Performance Metric record for **Payables Turnover Ratio (Deep Dive)** (PTRDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-payables-turnover-ratio-deep-dive`
- **Name:** Payables Turnover Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PTRDD

## 2. Definition

Payables Turnover Ratio (Deep Dive) (PTRDD) captures how efficiently resources are converted into outputs for organizations tracking financial statement analysis ratios (deep dive). It is a working-level control: thresholds trigger immediate operational response. It is defined as Cost of Sales / Average Payables; the result is stated in ratio (x:1 or x). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Cost of Sales / Average Payables
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** financial_statement_analysis_ratios_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4026 (batch 9)
