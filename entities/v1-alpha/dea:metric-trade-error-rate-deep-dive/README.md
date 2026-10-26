# dea:metric-trade-error-rate-deep-dive

Candidate Performance Metric record for **Trade Error Rate (Deep Dive)** (TER-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-trade-error-rate-deep-dive`
- **Name:** Trade Error Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TER-D

## 2. Definition

Within Investment Management - Portfolio Operations, Trade Error Rate (Deep Dive) (TER-D) is used to gauge the quality of outputs and outcomes. It provides the day-to-day signal that a process is running as designed. Its calculation is Trade Errors / Trades, measured in events per thousand or million (scaled). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Financial Services practice.

## Formula

```
TER-D = Trade Errors / Trades
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_management_portfolio_operations
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3014 (batch 7)
