# dea:metric-hidden-factory-ratio

Candidate Performance Metric record for **Hidden Factory Ratio** (HFR-SS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-hidden-factory-ratio`
- **Name:** Hidden Factory Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** HFR-SS

## 2. Definition

Hidden Factory Ratio (HFR-SS) captures how efficiently resources are converted into outputs for organizations tracking process capability & six sigma (deep dive). The formula is Capacity Consumed by Rework and Repair / Total Capacity - reported in percent (%). It is a standard measure in the Manufacturing sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the share of capacity consumed by rework, inspection, and workaround rather than value creation. The hidden factory is the tax of poor process quality paid in capacity. Ratios that exclude quality escapes understate the factory's size. Read with rework rate and process first-pass yield trend (Deep Dive).

## Formula

```
Capacity Consumed by Rework and Repair / Total Capacity
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** capability
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** process_capability_six_sigma_deep_dive
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4087 (batch 9)
