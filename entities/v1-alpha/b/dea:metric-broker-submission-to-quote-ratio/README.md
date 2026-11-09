# dea:metric-broker-submission-to-quote-ratio

Candidate Performance Metric record for **Broker Submission-to-Quote Ratio** (BSQR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-broker-submission-to-quote-ratio`
- **Name:** Broker Submission-to-Quote Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BSQR

## 2. Definition

Broker Submission-to-Quote Ratio (BSQR) captures how efficiently resources are converted into outputs for organizations tracking insurance underwriting. The formula is Quotes Issued / Broker Submissions - reported in percent (%). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Insurance sector.

## Formula

```
BSQR = Quotes Issued / Broker Submissions
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_underwriting
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1523 (batch 6)
