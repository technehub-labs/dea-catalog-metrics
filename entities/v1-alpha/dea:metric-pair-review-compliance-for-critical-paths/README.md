# dea:metric-pair-review-compliance-for-critical-paths

Candidate Performance Metric record for **Pair Review Compliance for Critical Paths** (PRCC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-pair-review-compliance-for-critical-paths`
- **Name:** Pair Review Compliance for Critical Paths
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PRCC

## 2. Definition

Pair Review Compliance for Critical Paths (PRCC) measures exposure to adverse outcomes in the Code Review & Peer Quality domain. The formula is Critical-Path Changes with Two Reviewers / Critical-Path Changes - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Software sector.

## Formula

```
Critical-Path Changes with Two Reviewers / Critical-Path Changes
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3203 (batch 7)
