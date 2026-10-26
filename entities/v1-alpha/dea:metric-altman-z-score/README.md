# dea:metric-altman-z-score

Candidate Performance Metric record for **Altman Z-Score** (ALTZ) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-altman-z-score`
- **Name:** Altman Z-Score
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ALTZ

## 2. Definition

Within Valuation & Corporate Finance Standard Measures, Altman Z-Score (ALTZ) is used to gauge exposure to adverse outcomes. It is defined as Composite Discriminant of Liquidity, Profitability, Leverage Ratios; the result is stated in score (points). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

The Altman Z-Score, from Edward I. Altman (1968), combines five weighted financial ratios (working capital, retained earnings, EBIT, market equity, sales) into one bankruptcy-risk score. Above 3.0 is the safe zone, 1.8-3.0 the grey zone, below 1.8 distress - and in Altman's original sample it predicted around 70-80% of corporate bankruptcies two years ahead. It was built for public manufacturers, so private-firm and non-manufacturer variants exist with different coefficients. Read it as an early-warning screen to trigger deeper review, not a verdict.

## Formula

```
Composite Discriminant of Liquidity, Profitability, Leverage Ratios
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** valuation_corporate_finance_standard_measures

## Attribution

- **Source credit:** Edward I. Altman, 1968

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4035 (batch 9)
