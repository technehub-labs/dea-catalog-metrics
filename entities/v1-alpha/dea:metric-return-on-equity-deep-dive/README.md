# dea:metric-return-on-equity-deep-dive

Candidate Performance Metric record for **Return on Equity (Deep Dive)** (ROEDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-return-on-equity-deep-dive`
- **Name:** Return on Equity (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ROEDD

## 2. Definition

Return on Equity (Deep Dive) (ROEDD) measures the economic value created or preserved in the Financial Statement Analysis Ratios (Deep Dive) domain. The formula is Net Income / Shareholder Equity - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures profit generated on shareholder capital. ROE is the headline shareholder return, but its decomposition matters: leverage-built ROE is fragile. Buyback-shrunken equity inflates ROE without operational improvement. Read with equity multiplier and return on invested capital (Deep Dive).

## Formula

```
ROEDD = Net Income / Shareholder Equity
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4033 (batch 9)
