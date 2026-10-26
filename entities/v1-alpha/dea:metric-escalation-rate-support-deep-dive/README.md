# dea:metric-escalation-rate-support-deep-dive

Candidate Performance Metric record for **Escalation Rate (Support Deep Dive)** (ESCR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-escalation-rate-support-deep-dive`
- **Name:** Escalation Rate (Support Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ESCR-D

## 2. Definition

Escalation Rate (Support Deep Dive) (ESCR-D) addresses the quality of outputs and outcomes and is a fixture of software product operations (deep dive) reporting. It provides the day-to-day signal that a process is running as designed. Its calculation is Escalated Tickets / Tickets, measured in percent (%). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Technology practice.

## Formula

```
ESCR-D = Escalated Tickets / Tickets
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2160 (batch 6)
