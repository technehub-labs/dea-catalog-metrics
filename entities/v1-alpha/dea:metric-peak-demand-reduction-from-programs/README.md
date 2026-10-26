# dea:metric-peak-demand-reduction-from-programs

Candidate Performance Metric record for **Peak Demand Reduction from Programs** (PDRP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-peak-demand-reduction-from-programs`
- **Name:** Peak Demand Reduction from Programs
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PDRP

## 2. Definition

A Utilities Customer Operations indicator, Peak Demand Reduction from Programs (PDRP) quantifies how effectively a process or entity achieves its intended outcome. It is defined as Load Reduction Achieved / Contracted Reduction; the result is stated in percent (%). In Utilities, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Peak demand reduction from programs measures the load shaved during system peak by demand response, efficiency, and load-management programs, and it is the capacity-value metric of demand-side management - each avoided megawatt of peak defers or displaces generation capacity investment, which is the entire economic justification for paying customers to reduce usage. The measurement subtlety is counterfactual: reduction is estimated against what consumption would have been, requiring baseline models (like the standard 10-of-10 non-event-day baseline) that are contested and gameable, since participants can inflate baselines to appear to reduce more. Verified-versus-claimed reduction gaps are well documented. Read with M&V (measurement and verification) methodology rigor, program cost per avoided MW versus capacity cost, event-day performance reliability (will customers respond when actually called?), and persistence of reductions across events.

## Formula

```
Load Reduction Achieved / Contracted Reduction
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** utilities_customer_operations
- **Sector:** utilities

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 964 (batch 3)
