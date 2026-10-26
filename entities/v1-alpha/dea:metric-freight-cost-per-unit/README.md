# dea:metric-freight-cost-per-unit

Candidate Performance Metric record for **Freight Cost per Unit** (FCPU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-freight-cost-per-unit`
- **Name:** Freight Cost per Unit
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FCPU

## 2. Definition

Freight Cost per Unit (FCPU) addresses how efficiently resources are converted into outputs and is a fixture of supply chain reporting. Its calculation is Total Freight Cost / Units Shipped, measured in currency per unit. It is applied across virtually every sector. Its value drives prioritization and resource reallocation among competing initiatives. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures average transportation cost per unit or shipment shipped. It matters because logistics cost is a controllable margin lever once volume is fixed. It can be cut cosmetically by shifting to slower modes that quietly degrade delivery reliability, or by unitizing loads to shrink apparent cost. Read with On-Time Delivery Rate and Total Landed Cost to balance cost cuts against service outcomes.

## Formula

```
Total Freight Cost / Units Shipped
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
- **Domain:** supply_chain

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 190 (batch 1)
