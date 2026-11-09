# dea:metric-actuarial-data-quality-score

Candidate Performance Metric record for **Actuarial Data Quality Score** (ADQS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-actuarial-data-quality-score`
- **Name:** Actuarial Data Quality Score
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ADQS

## 2. Definition

Actuarial Data Quality Score (ADQS) captures the quality of outputs and outcomes for organizations tracking actuarial & reserving. The formula is Weighted Data Quality Dimensions Score - reported in index (0-100 or normalized). It is a standard measure in the Insurance sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
ADQS = Weighted Data Quality Dimensions Score
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1530 (batch 6)
