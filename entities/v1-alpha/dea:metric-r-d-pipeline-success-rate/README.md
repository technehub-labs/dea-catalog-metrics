# dea:metric-r-d-pipeline-success-rate

Candidate Performance Metric record for **R&D Pipeline Success Rate** (RPSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-r-d-pipeline-success-rate`
- **Name:** R&D Pipeline Success Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RPSR

## 2. Definition

Within Pharmaceuticals & Life Sciences, R&D Pipeline Success Rate (RPSR) is used to gauge how effectively a process or entity achieves its intended outcome. The formula is Candidates Passing Stage / Candidates Entering Stage - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Pharmaceuticals sector.

## 3. Context

The share of pipeline candidates advancing through each development phase - the conversion metric of pharmaceutical R&D, whose strategic significance is the capital-intensity of failure: clinical development consumes the large majority of a drug's lifetime cost before the first revenue arrives, and phase-transition probabilities compound into industry-standard success rates from first-in-human to approval that remain modest. The metric's real analytical power is portfolio-level: expected value per pipeline asset is probability-weighted through these transition rates, so the assumed success rates drive the entire corporate valuation of a clinical-stage company. The honest comparisons are by modality and indication, since transition probabilities differ several-fold across therapeutic areas and molecule types - and pipeline mix shifts can move a blended success rate without any change in scientific capability. Read with the duration pairing: success at industry-median speed and success that slips years have very different NPVs, which is why pipeline metrics report both.

## Formula

```
Candidates Passing Stage / Candidates Entering Stage
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** pharmaceuticals_life_sciences
- **Sector:** pharmaceuticals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 478 (batch 1)
