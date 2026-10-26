# dea:metric-trade-decision-to-order-latency

Candidate Performance Metric record for **Trade Decision-to-Order Latency** (TDOL-T) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-trade-decision-to-order-latency`
- **Name:** Trade Decision-to-Order Latency
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** TDOL-T

## 2. Definition

Within Investment Research & Trading Operations, Trade Decision-to-Order Latency (TDOL-T) is used to gauge how efficiently resources are converted into outputs. The formula is Minutes from Decision to Order Placement - reported in minutes. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Lower values are better; each reduction is an improvement. It is a standard measure in the Financial Services sector.

## Formula

```
Minutes from Decision to Order Placement
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_research_trading_operations
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3035 (batch 7)
