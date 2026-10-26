# dea:metric-cost-per-hectare

Candidate Performance Metric record for **Cost per Hectare** (CPh) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-per-hectare`
- **Name:** Cost per Hectare
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CPh

## 2. Definition

Cost per Hectare (CPh) captures how efficiently resources are converted into outputs for organizations tracking agriculture & food processing. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Total Production Cost / Cultivated Hectares; the result is stated in currency per unit. It should be driven down, since lower readings signal healthier performance. In Agriculture & food, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures total production cost per cultivated hectare. It matters because it is the core unit economics benchmark for farming operations. It can be cut by skimping inputs whose absence shows up in yield rather than cost. Read with Yield per Hectare and Gross Margin per Hectare to confirm cost control does not sacrifice output.

## Formula

```
Total Production Cost / Cultivated Hectares
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** agriculture_food_processing
- **Sector:** agriculture_food

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 734 (batch 2)
