# dea:metric-significant-deficiency-closure-rate

Candidate Performance Metric record for **Significant Deficiency Closure Rate** (SDCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-significant-deficiency-closure-rate`
- **Name:** Significant Deficiency Closure Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SDCR

## 2. Definition

A Internal Controls & Financial Reporting Integrity indicator, Significant Deficiency Closure Rate (SDCR) quantifies conformance to standards, plans, or obligations. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Significant Deficiencies Remediated by Commit Date / Deficiencies - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how promptly identified significant deficiencies are remediated and re-tested. Open deficiencies are accumulating audit risk. Closure without re-test is hope, not remediation. Read with material weakness count and internal audit finding closure rate.

## Formula

```
SDCR = Significant Deficiencies Remediated by Commit Date / Deficiencies
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
- **Domain:** internal_controls_financial_reporting_integrity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3583 (batch 8)
