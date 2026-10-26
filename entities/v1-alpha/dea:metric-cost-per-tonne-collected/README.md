# dea:metric-cost-per-tonne-collected

Candidate Performance Metric record for **Cost per Tonne Collected** (CPTC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-per-tonne-collected`
- **Name:** Cost per Tonne Collected
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CPTC

## 2. Definition

Cost per Tonne Collected (CPTC) captures how efficiently resources are converted into outputs for organizations tracking waste & environmental services. Its calculation is Total Service Cost / Tonnes Collected, measured in currency per unit. It originates from and is most used in Environmental services practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Cost per tonne collected is the unit economics of waste collection - collection is labor-and-route intensive, so costs are driven by route density, vehicle cycles, and labor agreements rather than tonnage itself. The metric's diagnostic power comes from density awareness: suburban curbside collection costs multiples of dense urban or transfer-station economics, so cross-system comparisons mislead without density adjustment. Gaming risk sits in tonnage measurement: costs can fall because tonnage rose (dense routes or heavy materials), not because efficiency improved. Fuel and labor inflation hit this metric directly. Read with route density, stops per route-hour, truck utilization (full versus partial loads), and missed-collection rates (service quality traded against cost).

## Formula

```
Total Service Cost / Tonnes Collected
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** waste_environmental_services
- **Sector:** environmental_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 822 (batch 2)
