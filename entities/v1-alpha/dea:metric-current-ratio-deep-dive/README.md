# dea:metric-current-ratio-deep-dive

Candidate Performance Metric record for **Current Ratio (Deep Dive)** (CRDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-current-ratio-deep-dive`
- **Name:** Current Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CRDD

## 2. Definition

Current Ratio (Deep Dive) (CRDD) addresses exposure to adverse outcomes and is a fixture of financial statement analysis ratios (deep dive) reporting. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Current Assets / Current Liabilities, measured in ratio (x:1 or x). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures current assets relative to current liabilities. It is the basic test of short-term solvency. Ratio composition matters: inventory-heavy current assets are less liquid than they appear. Read with quick ratio (Deep Dive) and working capital ratio (Statement Analysis).

## Formula

```
Current Assets / Current Liabilities
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4015 (batch 9)
