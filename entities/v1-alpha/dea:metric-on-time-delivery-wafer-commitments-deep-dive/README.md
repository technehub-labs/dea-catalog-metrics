# dea:metric-on-time-delivery-wafer-commitments-deep-dive

Candidate Performance Metric record for **On-Time Delivery - Wafer Commitments (Deep Dive)** (OTD-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-on-time-delivery-wafer-commitments-deep-dive`
- **Name:** On-Time Delivery - Wafer Commitments (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** OTD-D

## 2. Definition

A Semiconductor Manufacturing (Deep Dive) indicator, On-Time Delivery - Wafer Commitments (Deep Dive) (OTD-D) quantifies conformance to standards, plans, or obligations. It is computed as Lots Delivered to Commit Date / Lots, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Semiconductors.

## 3. Context

Measures delivery of wafer lots against committed dates to internal and external customers. In allocation-constrained chip markets, schedule reliability is a customer-relationship asset that determines design wins for years, since customers qualify around suppliers who miss. OTD improvements from padded cycle-time estimates are honesty failures, not performance. Read with wafer fab cycle time (Deep Dive) and allocation governance for scarce capacity.

## Formula

```
Lots Delivered to Commit Date / Lots
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** semiconductor_manufacturing_deep_dive
- **Sector:** semiconductors

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2378 (batch 6)
