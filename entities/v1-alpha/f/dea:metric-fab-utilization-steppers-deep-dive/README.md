# dea:metric-fab-utilization-steppers-deep-dive

Candidate Performance Metric record for **Fab Utilization - Steppers (Deep Dive)** (FUS-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fab-utilization-steppers-deep-dive`
- **Name:** Fab Utilization - Steppers (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FUS-D

## 2. Definition

Within Semiconductor Manufacturing (Deep Dive), Fab Utilization - Steppers (Deep Dive) (FUS-D) is used to gauge the utilization or availability of capacity. Its calculation is Exposure Tool Productive Time / Available Time, measured in percent (%). It originates from and is most used in Semiconductors practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures utilization of lithography tools, the fab's capital-dominant and usually capacity-limiting equipment. Stepper utilization is the true throughput governor, and optimizing it (through WIP management, batching discipline, reticle availability) is worth more than most other fab programs. Utilization above sustainable levels trades against availability risk, since maintenance deferral on constraint tools is catastrophic. Read with queue-time compliance at the constraint and preventive maintenance schedule adherence.

## Formula

```
FUS-D = Exposure Tool Productive Time / Available Time
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2375 (batch 6)
