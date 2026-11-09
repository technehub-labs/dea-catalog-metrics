# dea:metric-readmission-rate-within-30-days

Candidate Performance Metric record for **Readmission Rate within 30 Days** (RR30) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-readmission-rate-within-30-days`
- **Name:** Readmission Rate within 30 Days
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RR30

## 2. Definition

Within Healthcare, Readmission Rate within 30 Days (RR30) is used to gauge the quality of outputs and outcomes. The formula is Readmissions within 30 Days / Discharges - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. It is a standard measure in the Healthcare sector.

## 3. Context

The share of discharges followed by unplanned readmission within thirty days - the metric that made care transitions a measure of quality rather than an administrative event, and the one that reimbursement regimes in several countries turned into a direct financial consequence for hospitals above threshold. Its strategic content is the distinction between planned and unplanned: only unplanned returns count, and the case-mix adjustment (readmission expected rates differ enormously by condition and patient complexity) is what makes cross-hospital comparison meaningful at all. The honest analysis decomposes by cause: readmissions driven by incomplete treatment, medication mismanagement, or absent follow-up are system failures; those driven by disease progression are clinical reality - and the metric cannot separate them, only flag the population for chart review. The classic gaming failure is upcoding severity at discharge, which raises expected readmission and lowers the penalty risk without improving care.

## Formula

```
RR30 = Readmissions within 30 Days / Discharges
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** healthcare
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 462 (batch 1)
