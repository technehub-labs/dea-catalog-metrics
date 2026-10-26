# dea:metric-support-tickets-per-1-000-users

Candidate Performance Metric record for **Support Tickets per 1,000 Users** (STK) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-support-tickets-per-1-000-users`
- **Name:** Support Tickets per 1,000 Users
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** STK

## 2. Definition

Support Tickets per 1,000 Users (STK) captures the quality of outputs and outcomes for organizations tracking product management. It is defined as Support Tickets / Users x 1,000; the result is stated in events per thousand or million (scaled). It is applied across virtually every sector. It is a working-level control: thresholds trigger immediate operational response. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
STK = Support Tickets / Users x 1,000
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** product_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 560 (batch 1)
