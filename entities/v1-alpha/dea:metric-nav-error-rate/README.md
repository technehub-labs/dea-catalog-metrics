# dea:metric-nav-error-rate

Candidate Performance Metric record for **NAV Error Rate** (NAVER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-nav-error-rate`
- **Name:** NAV Error Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** NAVER

## 2. Definition

A Investment Risk & Middle Office Operations indicator, NAV Error Rate (NAVER) quantifies the quality of outputs and outcomes. It provides the day-to-day signal that a process is running as designed. Its calculation is NAV Calculations with Error / NAVs Calculated, measured in events per thousand or million (scaled). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Investment management practice.

## Formula

```
NAV Calculations with Error / NAVs Calculated
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3461 (batch 7)
