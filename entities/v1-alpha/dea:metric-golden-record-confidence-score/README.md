# dea:metric-golden-record-confidence-score

Candidate Performance Metric record for **Golden Record Confidence Score** (GRCS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-golden-record-confidence-score`
- **Name:** Golden Record Confidence Score
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** GRCS

## 2. Definition

Golden Record Confidence Score (GRCS) addresses the quality of outputs and outcomes and is a fixture of data governance & stewardship reporting. It is defined as Composite of Completeness, Uniqueness, Timeliness for Golden Records; the result is stated in score (points). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how much the organization's surviving golden records can be trusted as authoritative. Confidence is earned through match accuracy, survivorship rules, and reconciliation evidence. Scores from the MDM vendor's own tooling are self-graded homework. Read with master data coverage rate and golden record trust score.

## Formula

```
GRCS = Composite of Completeness, Uniqueness, Timeliness for Golden Records
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3608 (batch 8)
