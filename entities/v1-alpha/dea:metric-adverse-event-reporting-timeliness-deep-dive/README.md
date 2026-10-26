# dea:metric-adverse-event-reporting-timeliness-deep-dive

Candidate Performance Metric record for **Adverse Event Reporting Timeliness (Deep Dive)** (AERT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-adverse-event-reporting-timeliness-deep-dive`
- **Name:** Adverse Event Reporting Timeliness (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** AERT

## 2. Definition

Adverse Event Reporting Timeliness (Deep Dive) (AERT) measures conformance to standards, plans, or obligations in the Pharma R&D & Clinical Trials domain. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as AE Reports Filed within Regulatory Window / Reports; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. In Pharmaceuticals, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures whether adverse events meet pharmacovigilance reporting deadlines. Timeliness is a hard regulatory obligation, and late AE reports are among the most common GxP enforcement triggers because they delay safety signals for the whole patient population. Watch for backlog-driven catch-up filings masking chronic lateness, and for severity-tier timing thresholds being misapplied. Read with signal detection cycle time and inspection findings in PV processes.

## Formula

```
AERT = AE Reports Filed within Regulatory Window / Reports
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** pharma_r_d_clinical_trials
- **Sector:** pharmaceuticals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1610 (batch 6)
