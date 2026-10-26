# dea:metric-debt-to-equity-ratio-deep-dive

Candidate Performance Metric record for **Debt-to-Equity Ratio (Deep Dive)** (DERDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-debt-to-equity-ratio-deep-dive`
- **Name:** Debt-to-Equity Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DERDD

## 2. Definition

Debt-to-Equity Ratio (Deep Dive) (DERDD) captures exposure to adverse outcomes for organizations tracking financial statement analysis ratios (deep dive). Its calculation is Total Debt / Total Equity, measured in ratio (x:1 or x). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures borrowed capital against shareholder capital. Leverage amplifies returns and fragility together. Market-value versions are more honest than book equity, which buybacks distort. Read with debt to equity (Deep Dive) and interest coverage ratio (Statement Analysis).

## Formula

```
Total Debt / Total Equity
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4020 (batch 9)
