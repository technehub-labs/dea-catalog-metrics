# dea:metric-payment-system-availability-deep-dive

Candidate Performance Metric record for **Payment System Availability (Deep Dive)** (PSA-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-payment-system-availability-deep-dive`
- **Name:** Payment System Availability (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PSA-D

## 2. Definition

Within Payments & Cards (Deep Dive), Payment System Availability (Deep Dive) (PSA-D) is used to gauge the utilization or availability of capacity. The formula is Available Minutes / Required Minutes - reported in percent (%). It is a standard measure in the Payments sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures uptime of payment processing across the authorization chain. Payments availability is binary at the moment of purchase: during an outage, every affected merchant's revenue stops, and switch-window degradation (batch settlement, reconciliation) matters as much as real-time authorization. Peak-load and incident-specific measurement beats monthly averages, since Black Friday failures are what stakeholders remember. Read with incident MTTR and capacity-stress test results.

## Formula

```
Available Minutes / Required Minutes
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** payments_cards_deep_dive
- **Sector:** payments

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2097 (batch 6)
