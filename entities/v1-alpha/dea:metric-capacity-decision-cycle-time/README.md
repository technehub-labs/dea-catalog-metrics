# dea:metric-capacity-decision-cycle-time

Candidate Performance Metric record for **Capacity Decision Cycle Time** (CDCT-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-capacity-decision-cycle-time`
- **Name:** Capacity Decision Cycle Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CDCT-S

## 2. Definition

Capacity Decision Cycle Time (CDCT-S) addresses how efficiently resources are converted into outputs and is a fixture of sales & operations planning reporting. Its calculation is Days to Resolve Identified Capacity Gap, measured in days. It is applied across virtually every sector. Its value drives prioritization and resource reallocation among competing initiatives. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the time to move through S&OP capacity decisions from signal to commitment. It matters because slow capacity decisions make S&OP a reporting exercise rather than a decision system. Cycle time can be cut by deferring hard decisions to executive escalation. Read with Scenario Planning Coverage and plan-versus-actual capacity decisions to confirm decisions are being made, not just discussed.

## Formula

```
Days to Resolve Identified Capacity Gap
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sales_operations_planning

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1294 (batch 5)
