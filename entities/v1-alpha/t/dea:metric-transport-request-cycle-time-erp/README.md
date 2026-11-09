# dea:metric-transport-request-cycle-time-erp

Candidate Performance Metric record for **Transport Request Cycle Time (ERP)** (TRCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-transport-request-cycle-time-erp`
- **Name:** Transport Request Cycle Time (ERP)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TRCT

## 2. Definition

A ERP & Enterprise Application Operations indicator, Transport Request Cycle Time (ERP) (TRCT) quantifies how efficiently resources are converted into outputs. It provides the day-to-day signal that a process is running as designed. Its calculation is Days from Development to Production Transport, measured in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
TRCT = Days from Development to Production Transport
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** erp_enterprise_application_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2172 (batch 6)
