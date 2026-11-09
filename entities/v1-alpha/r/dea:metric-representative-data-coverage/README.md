# dea:metric-representative-data-coverage

Candidate Performance Metric record for **Representative Data Coverage** (RDC-AI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-representative-data-coverage`
- **Name:** Representative Data Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RDC-AI

## 2. Definition

A AI Ethics, Fairness & Responsible AI indicator, Representative Data Coverage (RDC-AI) quantifies the quality of outputs and outcomes. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Population Segments Adequately Represented in Data / Segments - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures whether training and evaluation data adequately represent the populations the system serves. Representation gaps are the upstream cause of performance disparities - models failing on underrepresented groups - and coverage analysis is therefore both a fairness and a quality requirement. Coverage must be measured against deployment demographics, not convenience benchmarks. Read with fairness metric - equal opportunity gap (Deep Dive) and performance-by-segment evaluation.

## Formula

```
RDC-AI = Population Segments Adequately Represented in Data / Segments
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** ai_ethics_fairness_responsible_ai

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2579 (batch 7)
