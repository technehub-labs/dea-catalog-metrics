# dea:metric-cash-to-cash-cycle-time

Candidate Performance Metric record for **Cash-to-Cash Cycle Time** (C2C) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cash-to-cash-cycle-time`
- **Name:** Cash-to-Cash Cycle Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** C2C

## 2. Definition

Cash-to-Cash Cycle Time (C2C) measures how efficiently resources are converted into outputs in the Supply Chain domain. It is defined as DSO + DIO - DPO; the result is stated in days. It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

The number of days between paying suppliers for inventory and collecting cash from customers for it - the sum of days inventory outstanding, days sales outstanding, and days payables outstanding, with payables subtracted. It is the working capital metric that speaks in the language of the treasury, and it can be negative: companies that collect from customers before paying suppliers - most consumer retail on card payments - are effectively financed by their supply chain, which is why the metric is a strategic weapon as much as a measure. Every day removed is a day of permanent cash release, which is why improvement programs quote its cash value. The dark side is optimization transferred onto someone weaker: stretching payables to 120 days simply moves the financing burden upstream, a practice regulators now scrutinize.

## Formula

```
DSO + DIO - DPO
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** supply_chain

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 187 (batch 1)
