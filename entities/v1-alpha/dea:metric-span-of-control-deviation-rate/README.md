# dea:metric-span-of-control-deviation-rate

Candidate Performance Metric record for **Span of Control Deviation Rate** (SOCDEV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-span-of-control-deviation-rate`
- **Name:** Span of Control Deviation Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SOCDEV

## 2. Definition

A Operating Model & Process Health Deep Dive indicator, Span of Control Deviation Rate (SOCDEV) quantifies how efficiently resources are converted into outputs. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Units Outside Span Guideline / Units, measured in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how far actual spans deviate from design norms by role type. Chronic deviation signals either unrealistic design or organizational drift. Deviation is not inherently bad for specialist or senior-heavy functions. Read with operating model span and layer index and manager span of control (Deep Dive).

## Formula

```
Units Outside Span Guideline / Units
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** transformation
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** operating_model_process_health_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3501 (batch 7)
