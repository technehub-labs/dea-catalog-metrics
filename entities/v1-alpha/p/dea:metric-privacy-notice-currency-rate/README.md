# dea:metric-privacy-notice-currency-rate

Candidate Performance Metric record for **Privacy Notice Currency Rate** (PNCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-privacy-notice-currency-rate`
- **Name:** Privacy Notice Currency Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PNCR

## 2. Definition

Privacy Notice Currency Rate (PNCR) captures conformance to standards, plans, or obligations for organizations tracking data privacy & protection. The formula is Notices Updated within Change Window / Notices Requiring Update - reported in percent (%). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
PNCR = Notices Updated within Change Window / Notices Requiring Update
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** data_privacy_protection

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3661 (batch 8)
