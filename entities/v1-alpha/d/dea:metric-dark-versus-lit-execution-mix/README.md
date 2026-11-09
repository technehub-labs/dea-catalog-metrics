# dea:metric-dark-versus-lit-execution-mix

Candidate Performance Metric record for **Dark versus Lit Execution Mix** (DVLEM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-dark-versus-lit-execution-mix`
- **Name:** Dark versus Lit Execution Mix
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DVLEM

## 2. Definition

Within Investment Research & Trading Operations, Dark versus Lit Execution Mix (DVLEM) is used to gauge conformance to standards, plans, or obligations. The formula is Dark Venue Volume / Total Volume - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. It is a standard measure in the Financial Services sector.

## Formula

```
DVLEM = Dark Venue Volume / Total Volume
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_research_trading_operations
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3042 (batch 7)
