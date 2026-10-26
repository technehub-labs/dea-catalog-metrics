# dea:metric-value-stream-cost-to-serve

Candidate Performance Metric record for **Value Stream Cost-to-Serve** (VSCTS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-value-stream-cost-to-serve`
- **Name:** Value Stream Cost-to-Serve
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** VSCTS

## 2. Definition

Value Stream Cost-to-Serve (VSCTS) captures how efficiently resources are converted into outputs for organizations tracking operating model monitoring & design effectiveness. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Total Cost / Served Units across Stream; the result is stated in currency per unit. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the full accumulated cost of delivering a unit of value through the stream. Cost-to-serve exposes cross-subsidies that function-level P&Ls hide. Allocation methods materially change the picture, especially for shared platforms. Read with customer profitability segmentation index and process cost per transaction.

## Formula

```
Total Cost / Served Units across Stream
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3116 (batch 7)
