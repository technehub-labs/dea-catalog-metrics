# dea:metric-data-governance-maturity-score

Candidate Performance Metric record for **Data Governance Maturity Score** (DGMS-DG) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-governance-maturity-score`
- **Name:** Data Governance Maturity Score
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DGMS-DG

## 2. Definition

Data Governance Maturity Score (DGMS-DG) measures capability maturity or development in the Data Governance & Stewardship domain. The formula is Assessed Maturity Level per DAMA-Style Framework - reported in score (points). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures overall maturity of data governance across policy, stewardship, quality, and technology. Maturity trajectory matters more than the point score. Self-assessed maturity inflates a level versus external assessment. Read with data governance operating model maturity and critical data element governance coverage.

## Formula

```
DGMS-DG = Assessed Maturity Level per DAMA-Style Framework
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** capability
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** data_governance_stewardship

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3611 (batch 8)
