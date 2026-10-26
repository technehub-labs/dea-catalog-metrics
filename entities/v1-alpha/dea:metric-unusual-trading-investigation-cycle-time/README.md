# dea:metric-unusual-trading-investigation-cycle-time

Candidate Performance Metric record for **Unusual Trading Investigation Cycle Time** (UTICT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-unusual-trading-investigation-cycle-time`
- **Name:** Unusual Trading Investigation Cycle Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** UTICT

## 2. Definition

Unusual Trading Investigation Cycle Time (UTICT) measures exposure to adverse outcomes in the Investment Research & Trading Operations domain. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Days from Alert to Surveillance Case Close - reported in days. It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Financial Services sector.

## Formula

```
UTICT = Days from Alert to Surveillance Case Close
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_research_trading_operations
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3047 (batch 7)
