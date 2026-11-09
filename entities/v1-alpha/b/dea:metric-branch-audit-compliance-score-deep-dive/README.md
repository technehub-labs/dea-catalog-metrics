# dea:metric-branch-audit-compliance-score-deep-dive

Candidate Performance Metric record for **Branch Audit Compliance Score (Deep Dive)** (BACS-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-branch-audit-compliance-score-deep-dive`
- **Name:** Branch Audit Compliance Score (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BACS-D

## 2. Definition

Branch Audit Compliance Score (Deep Dive) (BACS-D) measures conformance to standards, plans, or obligations in the Retail Banking Branch Network (Deep Dive) domain. Its calculation is Composite Branch Audit Score, measured in score (points). Its value drives prioritization and resource reallocation among competing initiatives. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Banking practice.

## Formula

```
BACS-D = Composite Branch Audit Score
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** financial
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** retail_banking_branch_network_deep_dive
- **Sector:** banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2120 (batch 6)
