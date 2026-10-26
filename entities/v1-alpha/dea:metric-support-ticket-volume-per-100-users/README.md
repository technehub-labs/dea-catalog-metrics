# dea:metric-support-ticket-volume-per-100-users

Candidate Performance Metric record for **Support Ticket Volume per 100 Users** (STV100) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-support-ticket-volume-per-100-users`
- **Name:** Support Ticket Volume per 100 Users
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** STV100

## 2. Definition

Within Software Product Operations (Deep Dive), Support Ticket Volume per 100 Users (STV100) is used to gauge the quality of outputs and outcomes. The formula is Tickets / 100 Active Users - reported in events per thousand or million (scaled). It is a standard measure in the Technology sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Tickets / 100 Active Users
```

## Unit

- **Unit reference:** `dea:unit-events`
- **Unit:** events
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** software_product_operations_deep_dive
- **Sector:** technology

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2159 (batch 6)
