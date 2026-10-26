# dea:metric-calmar-ratio

Candidate Performance Metric record for **Calmar Ratio** (CALR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-calmar-ratio`
- **Name:** Calmar Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CALR

## 2. Definition

Calmar Ratio (CALR) captures exposure to adverse outcomes for organizations tracking investment performance measurement. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Annualized Return / Maximum Drawdown - reported in ratio (x:1 or x). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Investment management sector.

## 3. Context

The Calmar ratio, named for California Managed Accounts Reports (1990s), is annualized return divided by maximum drawdown - reward per unit of worst pain. Unlike Sharpe it speaks in capital terms: a Calmar of 2 means an investor earned twice the maximum peak-to-trough loss per year. Its limitation is the sample dependence of max drawdown - one long window with one deep crash dominates the metric, so it is usually computed on rolling 36-month windows and best used for comparing CTA-style or drawdown-averse strategies.

## Formula

```
Annualized Return / Maximum Drawdown
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
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_performance_measurement
- **Sector:** investment_management

## Attribution

- **Source credit:** California Managed Accounts Reports (Calmar), 1990s

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3445 (batch 7)
