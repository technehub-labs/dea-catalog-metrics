# dea:metric-protocol-deviation-rate

Candidate Performance Metric record for **Protocol Deviation Rate** (PDR-P) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-protocol-deviation-rate`
- **Name:** Protocol Deviation Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PDR-P

## 2. Definition

Protocol Deviation Rate (PDR-P) measures conformance to standards, plans, or obligations in the Pharma R&D & Clinical Trials domain. The formula is Deviations / Subjects Enrolled - reported in percent (%). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Lower values are better; each reduction is an improvement. It is a standard measure in the Pharmaceuticals sector.

## Formula

```
PDR-P = Deviations / Subjects Enrolled
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** pharma_r_d_clinical_trials
- **Sector:** pharmaceuticals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1608 (batch 6)
