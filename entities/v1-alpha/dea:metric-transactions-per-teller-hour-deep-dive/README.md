# dea:metric-transactions-per-teller-hour-deep-dive

Candidate Performance Metric record for **Transactions per Teller Hour (Deep Dive)** (TPTH-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-transactions-per-teller-hour-deep-dive`
- **Name:** Transactions per Teller Hour (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TPTH-D

## 2. Definition

Transactions per Teller Hour (Deep Dive) (TPTH-D) measures how efficiently resources are converted into outputs in the Retail Banking Branch Network (Deep Dive) domain. Its calculation is Teller Transactions / Teller Hours, measured in count (items per period). It provides the day-to-day signal that a process is running as designed. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Banking practice.

## Formula

```
TPTH-D = Teller Transactions / Teller Hours
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** retail_banking_branch_network_deep_dive
- **Sector:** banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2115 (batch 6)
