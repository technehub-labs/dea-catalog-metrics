# dea:metric-regulatory-report-filing-timeliness

Candidate Performance Metric record for **Regulatory Report Filing Timeliness** (RRFT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-regulatory-report-filing-timeliness`
- **Name:** Regulatory Report Filing Timeliness
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RRFT

## 2. Definition

Regulatory Report Filing Timeliness (RRFT) addresses conformance to standards, plans, or obligations and is a fixture of compliance monitoring & testing reporting. It is defined as Filings Submitted by Deadline / Filings Due; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures whether regulatory reports are filed within mandated deadlines. Late filings are pure self-inflicted enforcement risk. Timeliness that ignores accuracy (filed late-but-fast corrections) is partial compliance. Read with regulatory report error rate and regulatory finding closure rate.

## Formula

```
RRFT = Filings Submitted by Deadline / Filings Due
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** compliance_monitoring_testing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3562 (batch 8)
