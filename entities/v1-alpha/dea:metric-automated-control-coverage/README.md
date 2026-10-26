# dea:metric-automated-control-coverage

Candidate Performance Metric record for **Automated Control Coverage** (ACC-IC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-automated-control-coverage`
- **Name:** Automated Control Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ACC-IC

## 2. Definition

Automated Control Coverage (ACC-IC) captures how efficiently resources are converted into outputs for organizations tracking internal controls & financial reporting integrity. The formula is Key Controls Automated / Key Controls - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of key controls executed by systems rather than humans. Automated controls are consistent, evidence-complete, and cheap to test at scale. Automation without change control on the automation itself creates silent failure. Read with automated controls share and IT general control deficiency rate.

## Formula

```
Key Controls Automated / Key Controls
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3579 (batch 8)
