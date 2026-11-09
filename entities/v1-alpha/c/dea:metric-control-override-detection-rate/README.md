# dea:metric-control-override-detection-rate

Candidate Performance Metric record for **Control Override Detection Rate** (CODR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-control-override-detection-rate`
- **Name:** Control Override Detection Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CODR

## 2. Definition

A Internal Controls & Financial Reporting Integrity indicator, Control Override Detection Rate (CODR) quantifies exposure to adverse outcomes. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Overrides Detected by Monitoring / Overrides Occurring (Sampled); the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how often improper overrides of controls are detected. Overrides are the management-fraud vector: controls don't fail, they are switched off. Undetected overrides mean the detection control, not just the override, failed. Read with segregation of duties violation rate and fraud detection rate (Enterprise).

## Formula

```
CODR = Overrides Detected by Monitoring / Overrides Occurring (Sampled)
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** internal_controls_financial_reporting_integrity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3590 (batch 8)
