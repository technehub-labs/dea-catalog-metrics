# dea:metric-post-merge-revert-rate

Candidate Performance Metric record for **Post-Merge Revert Rate** (PMRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-post-merge-revert-rate`
- **Name:** Post-Merge Revert Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PMRR

## 2. Definition

A Code Review & Peer Quality indicator, Post-Merge Revert Rate (PMRR) quantifies the quality of outputs and outcomes. The formula is Reverted Merges / Merged Changes - reported in percent (%). It is a standard measure in the Software sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
PMRR = Reverted Merges / Merged Changes
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** code_review_peer_quality
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3193 (batch 7)
