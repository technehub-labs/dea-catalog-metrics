# dea:metric-review-defect-detection-yield

Candidate Performance Metric record for **Review Defect Detection Yield** (RDDY) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-review-defect-detection-yield`
- **Name:** Review Defect Detection Yield
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RDDY

## 2. Definition

Within Code Review & Peer Quality, Review Defect Detection Yield (RDDY) is used to gauge the quality of outputs and outcomes. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Defects Found in Review / (Defects in Review + Field) - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Software sector.

## Formula

```
Defects Found in Review / (Defects in Review + Field)
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** code_review_peer_quality
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3192 (batch 7)
