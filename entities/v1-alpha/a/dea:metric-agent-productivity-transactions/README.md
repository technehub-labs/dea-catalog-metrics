# dea:metric-agent-productivity-transactions

Candidate Performance Metric record for **Agent Productivity (Transactions)** (APT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-agent-productivity-transactions`
- **Name:** Agent Productivity (Transactions)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** APT

## 2. Definition

Agent Productivity (Transactions) (APT) captures how efficiently resources are converted into outputs for organizations tracking real estate brokerage. The formula is Closed Transactions / Agent per Period - reported in ratio (x:1 or x). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Real estate sector.

## 3. Context

Measures closed transactions per agent in real estate brokerage. It matters because agent productivity drives commission economics and office viability. Productivity counts can be inflated by team leader credit for junior work. Read with Pipeline-to-Closing Conversion and Commission per Transaction to confirm productivity reflects genuine selling effectiveness.

## Formula

```
APT = Closed Transactions / Agent per Period
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** real_estate_brokerage
- **Sector:** real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1013 (batch 3)
