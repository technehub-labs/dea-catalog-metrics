# dea:metric-demand-response-program-delivery

Candidate Performance Metric record for **Demand Response Program Delivery** (DRPD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-demand-response-program-delivery`
- **Name:** Demand Response Program Delivery
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DRPD

## 2. Definition

Demand Response Program Delivery (DRPD) captures the utilization or availability of capacity for organizations tracking utilities field operations & grid. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Curtailed Load vs Committed / Committed, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Utilities.

## 3. Context

Measures achieved load reduction against contracted demand response commitments. Demand response is dispatchable capacity that utilities are increasingly paid to deliver, and delivery shortfalls carry both financial penalties and resource-planning risk. Delivered megawatts must be verified against baseline consumption methodology, since baselines can be gamed in both directions. Read with event performance by customer segment and enrollment-to-event attrition.

## Formula

```
Curtailed Load vs Committed / Committed
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** utilities_field_operations_grid
- **Sector:** utilities

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1893 (batch 6)
