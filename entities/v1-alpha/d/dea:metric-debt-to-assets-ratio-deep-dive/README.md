# dea:metric-debt-to-assets-ratio-deep-dive

Candidate Performance Metric record for **Debt-to-Assets Ratio (Deep Dive)** (DARDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-debt-to-assets-ratio-deep-dive`
- **Name:** Debt-to-Assets Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DARDD

## 2. Definition

Debt-to-Assets Ratio (Deep Dive) (DARDD) measures exposure to adverse outcomes in the Financial Statement Analysis Ratios (Deep Dive) domain. The formula is Total Debt / Total Assets - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the proportion of the asset base financed by debt. It shows who really owns the assets: creditors or shareholders. Asset valuations (especially intangibles) drive comparability. Read with debt-to-equity ratio (Deep Dive) and equity multiplier.

## Formula

```
DARDD = Total Debt / Total Assets
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** financial_statement_analysis_ratios_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4021 (batch 9)
