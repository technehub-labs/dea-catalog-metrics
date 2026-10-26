# dea:metric-reviewer-load-balance-index

Candidate Performance Metric record for **Reviewer Load Balance Index** (RLBI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-reviewer-load-balance-index`
- **Name:** Reviewer Load Balance Index
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RLBI

## 2. Definition

A Code Review & Peer Quality indicator, Reviewer Load Balance Index (RLBI) quantifies the utilization or availability of capacity. The formula is Review Requests per Active Reviewer (Std Dev vs Mean) - reported in index (0-100 or normalized). It is a standard measure in the Software sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Review Requests per Active Reviewer (Std Dev vs Mean)
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3190 (batch 7)
