# dea:metric-peak-throughput-achieved

Candidate Performance Metric record for **Peak Throughput Achieved** (PTA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-peak-throughput-achieved`
- **Name:** Peak Throughput Achieved
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PTA

## 2. Definition

Peak Throughput Achieved (PTA) measures the utilization or availability of capacity in the Postal & Courier domain. It is defined as Peak Daily Items Processed / Design Capacity; the result is stated in percent (%). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Higher values are better; gains are read as improvement and losses as deterioration. In Postal & courier, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures maximum processing or delivery throughput sustained during peak periods. It matters because peak seasons determine capacity planning and reputation in postal and courier operations. Peak can be survived with emergency overtime and rentals that make the metric look met at unsustainable cost. Read with Peak Cost per Unit and Service Failure Rate during peaks to confirm throughput was healthy, not heroic.

## Formula

```
Peak Daily Items Processed / Design Capacity
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** postal_courier
- **Sector:** postal_courier

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 830 (batch 2)
