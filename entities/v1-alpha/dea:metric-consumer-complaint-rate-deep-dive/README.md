# dea:metric-consumer-complaint-rate-deep-dive

Candidate Performance Metric record for **Consumer Complaint Rate (Deep Dive)** (CCR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-consumer-complaint-rate-deep-dive`
- **Name:** Consumer Complaint Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CCR-D

## 2. Definition

Consumer Complaint Rate (Deep Dive) (CCR-D) captures the quality of outputs and outcomes for organizations tracking food & beverage manufacturing. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Complaints per Million Units Sold; the result is stated in events per thousand or million (scaled). It should be driven down, since lower readings signal healthier performance. In Food & Beverage, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures complaints per units sold, by category and severity. It is the market's free audit of food safety and quality, and complaint trends frequently detect problems before internal systems do. Foreign matter, allergen, and illness clusters deserve immediate escalation regardless of overall rate. Read with complaint-to-recall escalation history and batch-linked quality records.

## Formula

```
Complaints per Million Units Sold
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
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** food_beverage_manufacturing
- **Sector:** food_beverage

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1808 (batch 6)
