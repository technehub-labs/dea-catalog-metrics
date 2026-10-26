# dea:metric-value-stream-cycle-time-deep-dive

Candidate Performance Metric record for **Value Stream Cycle Time (Deep Dive)** (VSCT-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-value-stream-cycle-time-deep-dive`
- **Name:** Value Stream Cycle Time (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** VSCT-D

## 2. Definition

A Operating Model Monitoring & Design Effectiveness indicator, Value Stream Cycle Time (Deep Dive) (VSCT-D) quantifies how efficiently resources are converted into outputs. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is End-to-End Time across Value Stream, measured in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures end-to-end elapsed time across a value stream from demand to delivery. Value-stream time is the customer-experienced consequence of operating-model design. Improvement local to functions leaves value-stream queues untouched. Read with process cycle time trend and flow efficiency.

## Formula

```
End-to-End Time across Value Stream
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** operating_model_monitoring_design_effectiveness

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3115 (batch 7)
