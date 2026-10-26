# dea:metric-rebalancing-execution-cycle-time

Candidate Performance Metric record for **Rebalancing Execution Cycle Time** (REXCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-rebalancing-execution-cycle-time`
- **Name:** Rebalancing Execution Cycle Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** REXCT

## 2. Definition

A Investment Management - Portfolio Operations indicator, Rebalancing Execution Cycle Time (REXCT) quantifies how efficiently resources are converted into outputs. It provides the day-to-day signal that a process is running as designed. Its calculation is Days from Drift Trigger to Completed Rebalance, measured in days. It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Financial Services practice.

## Formula

```
Days from Drift Trigger to Completed Rebalance
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3011 (batch 7)
