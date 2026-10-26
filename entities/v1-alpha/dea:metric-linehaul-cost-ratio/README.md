# dea:metric-linehaul-cost-ratio

Candidate Performance Metric record for **Linehaul Cost Ratio** (LHR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-linehaul-cost-ratio`
- **Name:** Linehaul Cost Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LHR

## 2. Definition

A Logistics & Transportation indicator, Linehaul Cost Ratio (LHR) quantifies how efficiently resources are converted into outputs. It is defined as Linehaul Cost / Total Logistics Cost; the result is stated in percent (%). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. In Logistics, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures linehaul transportation cost as a percentage of revenue or total logistics cost. It matters because linehaul is typically the largest controllable logistics block. It can be cut cosmetically by shifting cost into accessorial fees or shifting slow modes that damage service. Read with Freight Cost per Unit and On-Time Delivery Rate to confirm cost reduction does not trade away promises.

## Formula

```
Linehaul Cost / Total Logistics Cost
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** logistics_transportation
- **Sector:** logistics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 206 (batch 1)
