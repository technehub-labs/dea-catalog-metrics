# dea:metric-review-comment-resolution-rate

Candidate Performance Metric record for **Review Comment Resolution Rate** (RCR-PR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-review-comment-resolution-rate`
- **Name:** Review Comment Resolution Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RCR-PR

## 2. Definition

Review Comment Resolution Rate (RCR-PR) addresses the quality of outputs and outcomes and is a fixture of code review & peer quality reporting. The formula is Comments Resolved before Merge / Comments Raised - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Software sector.

## Formula

```
RCR-PR = Comments Resolved before Merge / Comments Raised
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3205 (batch 7)
