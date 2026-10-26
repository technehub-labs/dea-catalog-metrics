# dea:metric-operational-loss-event-rate

Candidate Performance Metric record for **Operational Loss Event Rate** (OLER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-operational-loss-event-rate`
- **Name:** Operational Loss Event Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** OLER

## 2. Definition

A Investment Risk & Middle Office Operations indicator, Operational Loss Event Rate (OLER) quantifies exposure to adverse outcomes. It provides the day-to-day signal that a process is running as designed. Its calculation is Operational Loss Events per 1,000 Trades, measured in events per thousand or million (scaled). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Investment management practice.

## Formula

```
Operational Loss Events per 1,000 Trades
```

## Unit

- **Unit reference:** `dea:unit-events`
- **Unit:** events
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_risk_middle_office_operations
- **Sector:** investment_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3472 (batch 7)
