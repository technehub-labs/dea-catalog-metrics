# dea:metric-target-price-accuracy-band

Candidate Performance Metric record for **Target Price Accuracy Band** (TPAB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-target-price-accuracy-band`
- **Name:** Target Price Accuracy Band
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TPAB

## 2. Definition

A Investment Research & Trading Operations indicator, Target Price Accuracy Band (TPAB) quantifies the quality of outputs and outcomes. It is computed as Actual Prices within Target Band / Targets Sampled, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Financial Services.

## 3. Context

Measures how often realized prices fall within analysts' stated target ranges over their stated horizons. Target accuracy disciplines one of the most gamed outputs in research. Targets updated quietly after the fact inflate apparent accuracy. Read with analyst recommendation hit rate and excess return over benchmark.

## Formula

```
Actual Prices within Target Band / Targets Sampled
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_research_trading_operations
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3031 (batch 7)
