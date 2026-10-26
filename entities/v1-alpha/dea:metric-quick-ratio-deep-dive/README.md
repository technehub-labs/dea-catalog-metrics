# dea:metric-quick-ratio-deep-dive

Candidate Performance Metric record for **Quick Ratio (Deep Dive)** (QRDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-quick-ratio-deep-dive`
- **Name:** Quick Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** QRDD

## 2. Definition

Within Financial Statement Analysis Ratios (Deep Dive), Quick Ratio (Deep Dive) (QRDD) is used to gauge exposure to adverse outcomes. Its calculation is (Current Assets - Inventory) / Current Liabilities, measured in ratio (x:1 or x). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures liquid current assets (excluding inventory) against current liabilities. The acid test strips the least liquid assets out of the solvency question. Excluding receivables (cash ratio) is stricter still, and often more honest in distress. Read with current ratio (Deep Dive) and cash ratio (Deep Dive).

## Formula

```
(Current Assets - Inventory) / Current Liabilities
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** financial_statement_analysis_ratios_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4016 (batch 9)
