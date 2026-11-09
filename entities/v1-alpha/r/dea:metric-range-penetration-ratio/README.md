# dea:metric-range-penetration-ratio

Candidate Performance Metric record for **Range Penetration Ratio** (RPR-PAY) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-range-penetration-ratio`
- **Name:** Range Penetration Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RPR-PAY

## 2. Definition

Range Penetration Ratio (RPR-PAY) measures conformance to standards, plans, or obligations in the Standard Workforce & Pay Metrics domain. The formula is (Salary - Range Minimum) / (Range Maximum - Minimum) - reported in percent (%). It is applied across virtually every sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Values outside the intended band, on either side, warrant investigation.

## Formula

```
RPR-PAY = (Salary - Range Minimum) / (Range Maximum - Minimum)
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** standard_workforce_pay_metrics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4117 (batch 9)
