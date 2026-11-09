# dea:metric-new-product-ramp-yield

Candidate Performance Metric record for **New Product Ramp Yield** (NPRY) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-new-product-ramp-yield`
- **Name:** New Product Ramp Yield
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** NPRY

## 2. Definition

New Product Ramp Yield (NPRY) captures how effectively a process or entity achieves its intended outcome for organizations tracking semiconductor & electronics. It is defined as Yield at Ramp Milestone / Target Yield; the result is stated in percent (%). In Electronics & semiconductors, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

New product ramp yield measures how quickly a new design reaches mature yield levels after production start, and it is the time-to-revenue metric of semiconductor product introductions - leading-edge products carry enormous wafer cost, so slow yield ramps mean selling high-cost wafers or holding inventory until economics improve. The learning-curve dynamic is structural: yields start low and improve with engineering feedback cycles, so ramp speed is really engineering iteration speed. Design-for-manufacturability shortens ramps by making products tolerant of process variation, linking design decisions to manufacturing economics. Read with yield learning rate by week of ramp, design-versus-process attribution of yield loss, and cost per die trajectory to profitability crossover.

## Formula

```
NPRY = Yield at Ramp Milestone / Target Yield
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** semiconductor_electronics
- **Sector:** electronics_semiconductors

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 915 (batch 3)
