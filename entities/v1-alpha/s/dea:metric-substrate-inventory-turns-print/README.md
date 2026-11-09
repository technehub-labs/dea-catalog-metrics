# dea:metric-substrate-inventory-turns-print

Candidate Performance Metric record for **Substrate Inventory Turns (Print)** (SIT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-substrate-inventory-turns-print`
- **Name:** Substrate Inventory Turns (Print)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SIT

## 2. Definition

A Printing & Publishing indicator, Substrate Inventory Turns (Print) (SIT) quantifies how efficiently resources are converted into outputs. The formula is Substrate Consumed / Average Substrate Inventory - reported in times per period. It is a standard measure in the Printing & publishing sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how often paper and substrate inventory turns over. It matters because substrate ties up cash and risks obsolescence as specs change. Turns can be improved by spot-buying at premium prices to keep stock low. Read with Total Landed Cost for substrate and Stockout-induced missed deadlines to confirm lean stock is economic.

## Formula

```
SIT = Substrate Consumed / Average Substrate Inventory
```

## Unit

- **Unit reference:** `dea:unit-times`
- **Unit:** times
- **Unit label (as published):** times per period

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** printing_publishing
- **Sector:** printing_publishing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1264 (batch 4)
