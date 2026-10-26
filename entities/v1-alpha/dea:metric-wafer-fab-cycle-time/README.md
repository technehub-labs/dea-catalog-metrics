# dea:metric-wafer-fab-cycle-time

Candidate Performance Metric record for **Wafer Fab Cycle Time** (WFCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-wafer-fab-cycle-time`
- **Name:** Wafer Fab Cycle Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** WFCT

## 2. Definition

Wafer Fab Cycle Time (WFCT) addresses how efficiently resources are converted into outputs and is a fixture of semiconductor & electronics reporting. The formula is Days from Wafer Start to Finished Wafer - reported in days. It is a standard measure in the Electronics & semiconductors sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Wafer fab cycle time measures days from wafer start to finished wafer, and it is the flow metric that counters semiconductor fabs' natural tendency toward local optimization - individual tool utilization can be maximized while fab cycle time explodes, which is why cycle time (not utilization) is the true fab health measure. Wafers traverse hundreds of process steps through constraint tools, making fabs textbook theory-of-constraints environments where WIP control at the bottleneck governs everything. Cycle time interacts with yield (long queuing adds defect exposure risk) and with flexibility (short cycle time enables mix shifts). Read with WIP levels against constraint capacity, line yield, on-time delivery to downstream assembly, and cycle-time variability rather than just mean.

## Formula

```
Days from Wafer Start to Finished Wafer
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
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** semiconductor_electronics
- **Sector:** electronics_semiconductors

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 905 (batch 3)
