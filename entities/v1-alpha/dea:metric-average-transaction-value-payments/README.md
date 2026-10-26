# dea:metric-average-transaction-value-payments

Candidate Performance Metric record for **Average Transaction Value (Payments)** (ATV-P) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-transaction-value-payments`
- **Name:** Average Transaction Value (Payments)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ATV-P

## 2. Definition

A Payments & Fintech indicator, Average Transaction Value (Payments) (ATV-P) quantifies the economic value created or preserved. It is defined as Total Processed Value / Transaction Count; the result is stated in currency value. Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. In Payments & fintech, it is a recognized element of the standard performance toolkit.

## 3. Context

Average transaction value divides processed volume by transaction count, and in payments it is a mix metric more than a performance metric - it shifts with merchant portfolio composition, seasonal retail cycles, and macro spending patterns, so a decline can reflect client mix rather than anything the operator did. Its strategic uses are real: pricing (per-transaction fees hurt low-ATV merchants, ad-valorem fees hurt high-ATV ones), risk (higher ATV raises fraud exposure per event), and product design. Trends within a stable merchant base are more informative than blended figures. Read with transaction count growth separately - volume driven by count versus by ticket size signals different economic dynamics.

## Formula

```
Total Processed Value / Transaction Count
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** payments_fintech
- **Sector:** payments_fintech

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 781 (batch 2)
