# dea:metric-cognitive-complexity

Candidate Performance Metric record for **Cognitive Complexity** (CGCQ) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cognitive-complexity`
- **Name:** Cognitive Complexity
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CGCQ

## 2. Definition

Within Code Quality & Static Analysis, Cognitive Complexity (CGCQ) is used to gauge the quality of outputs and outcomes. It is a working-level control: thresholds trigger immediate operational response. It is defined as Complexity Weighted for Human Understandability; the result is stated in score (points). It should be driven down, since lower readings signal healthier performance. In Software, it is a recognized element of the standard performance toolkit.

## Formula

```
CGCQ = Complexity Weighted for Human Understandability
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** code_quality_static_analysis
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4176 (batch 9)
