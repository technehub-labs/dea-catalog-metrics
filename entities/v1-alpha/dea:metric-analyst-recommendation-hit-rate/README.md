# dea:metric-analyst-recommendation-hit-rate

Candidate Performance Metric record for **Analyst Recommendation Hit Rate** (ARHR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-analyst-recommendation-hit-rate`
- **Name:** Analyst Recommendation Hit Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ARHR

## 2. Definition

Analyst Recommendation Hit Rate (ARHR) captures how effectively a process or entity achieves its intended outcome for organizations tracking investment research & trading operations. It is computed as Recommendations Meeting Target Return / Recommendations, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Financial Services.

## 3. Context

Measures how often analyst recommendations are followed by the expected price direction. It is the accountability loop for the research function. Short-window hit rates are statistically noisy and prone to momentum-driven flattery. Read with target price accuracy band and research coverage ratio.

## Formula

```
Recommendations Meeting Target Return / Recommendations
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** effectiveness
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3030 (batch 7)
