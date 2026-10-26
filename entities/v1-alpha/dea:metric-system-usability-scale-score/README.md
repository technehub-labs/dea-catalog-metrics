# dea:metric-system-usability-scale-score

Candidate Performance Metric record for **System Usability Scale Score** (SUS-UX) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-system-usability-scale-score`
- **Name:** System Usability Scale Score
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SUS-UX

## 2. Definition

System Usability Scale Score (SUS-UX) measures the quality of outputs and outcomes in the UX & Design Systems domain. The formula is Standardized 10-Item Usability Questionnaire Score - reported in score (points). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

The System Usability Scale, created by John Brooke (1996), is a 10-item questionnaire producing a 0-100 usability score - the most widely used quick-read usability instrument in the industry. Scores above 68 are conventionally above average; below 51 is poor. Its strengths are speed, comparability across products, and a large reference corpus; its limits are that it measures perceived usability, not actual task success. Best practice is pairing SUS with task-based testing, because users sometimes rate pretty-but-unusable systems highly on first impression.

## Formula

```
Standardized 10-Item Usability Questionnaire Score
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** ux_design_systems

## Attribution

- **Source credit:** John Brooke (System Usability Scale, 1996)

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3267 (batch 7)
