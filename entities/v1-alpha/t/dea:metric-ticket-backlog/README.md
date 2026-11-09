# dea:metric-ticket-backlog

Candidate Performance Metric record for **Ticket Backlog** (TBK) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ticket-backlog`
- **Name:** Ticket Backlog
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TBK

## 2. Definition

Within IT Service Management, Ticket Backlog (TBK) is used to gauge the utilization or availability of capacity. It provides the day-to-day signal that a process is running as designed. Its calculation is Open Tickets Aged beyond Target, measured in count (items per period). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
TBK = Open Tickets Aged beyond Target
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** it_service_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 309 (batch 1)
