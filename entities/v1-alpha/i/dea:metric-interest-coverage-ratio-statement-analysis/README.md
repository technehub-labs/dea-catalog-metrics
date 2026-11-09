# dea:metric-interest-coverage-ratio-statement-analysis

Candidate Performance Metric record for **Interest Coverage Ratio (Statement Analysis)** (ICRDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-interest-coverage-ratio-statement-analysis`
- **Name:** Interest Coverage Ratio (Statement Analysis)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ICRDD

## 2. Definition

A Financial Statement Analysis Ratios (Deep Dive) indicator, Interest Coverage Ratio (Statement Analysis) (ICRDD) quantifies exposure to adverse outcomes. The formula is EBIT / Interest Expense - reported in ratio (x:1 or x). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures earnings available to service interest expense. Coverage deteriorates long before default; it is the early warning on the credit curve. Coverage computed on peak-cycle earnings is a fair-weather number. Read with debt service coverage ratio (Deep Dive) and debt-to-equity ratio (Deep Dive).

## Formula

```
ICRDD = EBIT / Interest Expense
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4023 (batch 9)
