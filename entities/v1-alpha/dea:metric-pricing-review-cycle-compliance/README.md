# dea:metric-pricing-review-cycle-compliance

Candidate Performance Metric record for **Pricing Review Cycle Compliance** (PRCC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-pricing-review-cycle-compliance`
- **Name:** Pricing Review Cycle Compliance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PRCC

## 2. Definition

Within Actuarial & Reserving, Pricing Review Cycle Compliance (PRCC) is used to gauge conformance to standards, plans, or obligations. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Segments Reviewed within Cycle / Segments Due - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Insurance sector.

## Formula

```
PRCC = Segments Reviewed within Cycle / Segments Due
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** actuarial_reserving
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1536 (batch 6)
