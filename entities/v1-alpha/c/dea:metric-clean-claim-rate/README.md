# dea:metric-clean-claim-rate

Candidate Performance Metric record for **Clean Claim Rate** (CCR-H) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-clean-claim-rate`
- **Name:** Clean Claim Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CCR-H

## 2. Definition

Clean Claim Rate (CCR-H) measures the quality of outputs and outcomes in the Healthcare Revenue Cycle domain. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Claims Accepted on First Submission / Claims Submitted - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Healthcare sector.

## 3. Context

Clean claim rate measures the share of claims accepted by payers on first submission without edits, rejections, or requests for information, and it is the upstream determinant of almost every downstream revenue-cycle metric - clean claims pay faster, cost less, and rarely age past 90 days. Because each rejected claim costs real money to rework (industry estimates put rework cost at roughly $25 per claim) and delays cash by weeks, prevention at the source beats heroic rework. Root causes concentrate at the front end: registration errors, eligibility mismatches, and coding accuracy account for most rejections. Read with first-pass resolve rate (a claim accepted can still deny on adjudication), denial rate by reason code, and front-end error attribution from claim edit audits.

## Formula

```
CCR-H = Claims Accepted on First Submission / Claims Submitted
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** healthcare_revenue_cycle
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 872 (batch 3)
