# dea:metric-well-completion-cycle-time

Candidate Performance Metric record for **Well Completion Cycle Time** (WCCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-well-completion-cycle-time`
- **Name:** Well Completion Cycle Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** WCCT

## 2. Definition

Well Completion Cycle Time (WCCT) measures how efficiently resources are converted into outputs in the Oil & Gas domain. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Days from Spud to Production Start, measured in days. It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Oil & gas practice.

## 3. Context

Well completion cycle time measures days from drilling finished to production ready, and in shale it is the pace metric of the factory-model development - pad drilling economics depend on moving crews and equipment through standardized completion sequences quickly, with each day of rig or crew standby carrying substantial spread cost. Cycle time compresses with logistics coordination (sand, water, and crew scheduling are the binding constraints) and with zipper-frac operational choreography. The trade-off to watch is quality: faster completions that degrade stage isolation or leave wells under-stimulated trade time now for production later. Read with cost per completed well, completion crew utilization, stage-per-day throughput, and 90-day production per foot against cycle time to test whether speed is costing performance.

## Formula

```
Days from Spud to Production Start
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** oil_gas
- **Sector:** oil_gas

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 888 (batch 3)
