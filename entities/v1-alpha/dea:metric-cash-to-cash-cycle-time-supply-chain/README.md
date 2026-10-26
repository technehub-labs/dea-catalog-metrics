# dea:metric-cash-to-cash-cycle-time-supply-chain

Candidate Performance Metric record for **Cash-to-Cash Cycle Time (Supply Chain)** (C2C) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cash-to-cash-cycle-time-supply-chain`
- **Name:** Cash-to-Cash Cycle Time (Supply Chain)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** C2C

## 2. Definition

Cash-to-Cash Cycle Time (Supply Chain) (C2C) measures how efficiently resources are converted into outputs in the Supply Chain Standard Measures (Deep Dive) domain. Its calculation is DIO + DSO - DPO across Chain, measured in days. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures days from paying suppliers to collecting from customers across the chain. It is the supply chain's master working capital metric. Each inventory day removed is financing freed. Read with cash conversion cycle (Working Capital) and inventory turns (supply chain).

## Formula

```
DIO + DSO - DPO across Chain
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** supply_chain_standard_measures_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4262 (batch 10)
