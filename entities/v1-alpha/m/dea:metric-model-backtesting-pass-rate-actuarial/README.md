# dea:metric-model-backtesting-pass-rate-actuarial

Candidate Performance Metric record for **Model Backtesting Pass Rate (Actuarial)** (MBPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-model-backtesting-pass-rate-actuarial`
- **Name:** Model Backtesting Pass Rate (Actuarial)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MBPR

## 2. Definition

Model Backtesting Pass Rate (Actuarial) (MBPR) addresses the quality of outputs and outcomes and is a fixture of actuarial & reserving reporting. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Models Meeting Backtest Tolerances / Models Tested, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Insurance.

## 3. Context

Measures how often reserving and pricing models, tested against later actuals, perform within tolerance. Backtesting is the falsifiability requirement for actuarial credibility, separating models that predict from models that rationalize. Tolerance setting is the honesty battleground - wide tolerances make everything pass. Segment by line and maturity, and investigate clustering of failures in specific exposure types. Read with reserve runoff error rate and actuarial model validation coverage.

## Formula

```
MBPR = Models Meeting Backtest Tolerances / Models Tested
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** actuarial_reserving
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1529 (batch 6)
