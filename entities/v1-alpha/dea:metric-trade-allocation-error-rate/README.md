# dea:metric-trade-allocation-error-rate

Candidate Performance Metric record for **Trade Allocation Error Rate** (TAER-T) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-trade-allocation-error-rate`
- **Name:** Trade Allocation Error Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** TAER-T

## 2. Definition

Within Investment Research & Trading Operations, Trade Allocation Error Rate (TAER-T) is used to gauge the quality of outputs and outcomes. It is a working-level control: thresholds trigger immediate operational response. It is defined as Allocation Errors / Allocations; the result is stated in events per thousand or million (scaled). It should be driven down, since lower readings signal healthier performance. In Financial Services, it is a recognized element of the standard performance toolkit.

## Formula

```
Allocation Errors / Allocations
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
- **Domain:** investment_research_trading_operations
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3043 (batch 7)
