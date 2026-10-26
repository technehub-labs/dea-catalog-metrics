# dea:metric-defects-per-million-opportunities

Candidate Performance Metric record for **Defects per Million Opportunities** (DPMO) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-defects-per-million-opportunities`
- **Name:** Defects per Million Opportunities
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DPMO

## 2. Definition

A Quality Management indicator, Defects per Million Opportunities (DPMO) quantifies the quality of outputs and outcomes. It is defined as Defects / (Units x Opportunities) x 1,000,000; the result is stated in events per thousand or million (scaled). Its trend is watched by senior leadership as an early signal of structural performance shifts. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

The count of defects normalized to a million opportunities - the normalization that made cross-process quality comparison possible by recognizing that complex products offer more chances to fail than simple ones. It is the native language of Six Sigma: process sigma levels are read directly from DPMO, with 3.4 defects per million opportunities defining the namesake six-sigma level, and the scale's strategic power is that a single metric spans everything from invoicing accuracy to solder joints. Opportunity counting is the metric's known weakness - the number of opportunities per unit is a convention, and inflating opportunities lowers DPMO without any real change - which is why disciplined organizations fix opportunity definitions per process family. Read the rate with defect severity: a low DPMO dominated by critical defects is worse than a higher rate of cosmetic ones.

## Formula

```
Defects / (Units x Opportunities) x 1,000,000
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** capability
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** quality_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 233 (batch 1)
