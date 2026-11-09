# dea:metric-key-control-operating-effectiveness-rate

Candidate Performance Metric record for **Key Control Operating Effectiveness Rate** (KCOER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-key-control-operating-effectiveness-rate`
- **Name:** Key Control Operating Effectiveness Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** KCOER

## 2. Definition

A Internal Controls & Financial Reporting Integrity indicator, Key Control Operating Effectiveness Rate (KCOER) quantifies the quality of outputs and outcomes. Its calculation is Key Controls Operating Effectively / Key Controls Tested, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures whether key controls operated as designed throughout the period. Effectiveness is tested evidence, not attestation. Exception-based testing that samples only quiet periods overstates effectiveness. Read with key control design adequacy rate and control override detection rate.

## Formula

```
KCOER = Key Controls Operating Effectively / Key Controls Tested
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** quality
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3576 (batch 8)
