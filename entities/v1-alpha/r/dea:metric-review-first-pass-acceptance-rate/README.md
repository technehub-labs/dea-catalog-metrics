# dea:metric-review-first-pass-acceptance-rate

Candidate Performance Metric record for **Review First-Pass Acceptance Rate** (RFPAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-review-first-pass-acceptance-rate`
- **Name:** Review First-Pass Acceptance Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RFPAR

## 2. Definition

Review First-Pass Acceptance Rate (RFPAR) measures the quality of outputs and outcomes in the Code Review & Peer Quality domain. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Reviews Approved without Change Requests / Reviews - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Software sector.

## Formula

```
RFPAR = Reviews Approved without Change Requests / Reviews
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3188 (batch 7)
