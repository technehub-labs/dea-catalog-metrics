# dea:metric-logistics-cost-per-vehicle

Candidate Performance Metric record for **Logistics Cost per Vehicle** (LCV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-logistics-cost-per-vehicle`
- **Name:** Logistics Cost per Vehicle
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LCV

## 2. Definition

Logistics Cost per Vehicle (LCV) measures how efficiently resources are converted into outputs in the Automotive domain. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Total Inbound and Outbound Logistics Cost / Vehicles Sold - reported in currency per unit. It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Automotive sector.

## 3. Context

Measures total inbound and outbound logistics cost per vehicle delivered. It matters because finished vehicle logistics is a large per-unit cost in automotive. Shifting cost to suppliers (who recover it in price) can understate the true number. Read with Total Landed Cost and Delivery Lead Time to confirm cost and service are both honest.

## Formula

```
Total Inbound and Outbound Logistics Cost / Vehicles Sold
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
- **Domain:** automotive
- **Sector:** automotive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 751 (batch 2)
