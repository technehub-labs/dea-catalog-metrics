# dea:metric-capacity-utilization

Candidate Performance Metric record for **Capacity Utilization** (CU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-capacity-utilization`
- **Name:** Capacity Utilization
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CU

## 2. Definition

Within Operations, Capacity Utilization (CU) is used to gauge the utilization or availability of capacity. It is defined as Actual Output / Maximum Possible Output; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Actual output as a share of maximum sustainable output - the metric at the hinge of operating strategy, because almost every plant economics problem is a utilization problem. Below roughly 70 percent, fixed costs are spread so thin that margin collapses even with disciplined spending; above sustained high levels, the strategic problem flips to bottleneck risk and the case for capital expenditure, and understanding which side of that hinge the business sits on is the point of tracking it. It is also a macroeconomic indicator - statistical agencies publish economy-wide utilization as an inflation signal, since tight capacity transmits wage and input pressure into prices. Internally, read it by constraint: the utilization of the bottleneck operation is the only one that sets system output, which is the core insight of the theory of constraints.

## Formula

```
Actual Output / Maximum Possible Output
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 153 (batch 1)
