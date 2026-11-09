# dea:metric-process-cycle-efficiency

Candidate Performance Metric record for **Process Cycle Efficiency** (PCE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-process-cycle-efficiency`
- **Name:** Process Cycle Efficiency
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PCE

## 2. Definition

A Operations indicator, Process Cycle Efficiency (PCE) quantifies how efficiently resources are converted into outputs. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Value-Added Time / Total Cycle Time; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures value-added time as a percentage of total process lead time. It matters because it quantifies how much of a process is waste waiting to be removed. Teams can inflate it by reclassifying waiting or handoff time as value-added in the mapping workshop. Read with Order Fulfillment Cycle Time and Bottleneck Utilization to target the constraints where lean effort pays off.

## Formula

```
PCE = Value-Added Time / Total Cycle Time
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 156 (batch 1)
