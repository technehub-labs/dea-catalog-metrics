# dea:metric-product-quality-score

Candidate Performance Metric record for **Product-Quality Score** (PQS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-product-quality-score`
- **Name:** Product-Quality Score
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PQS

## 2. Definition

Product-Quality Score (PQS) addresses the quality of outputs and outcomes and is a fixture of product management reporting. The formula is Weighted Index of Defects, Performance, Satisfaction - reported in index (0-100 or normalized). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

A composite assessment of product quality across dimensions - typically defect rates, reliability measures, user-perceived quality ratings, and support-ticket signatures - combined into a single tracked index. Its strategic significance is what it makes comparable: engineering defect metrics and user-experience ratings live in different languages, and a composite lets quality be managed at roadmap level - quality work competes with feature work for the same release capacity, and this metric is how that competition is arbitrated. The weighting is the honesty question: a composite that overweights easy-to-count dimensions (crashes) and underweights the ones users feel (perceived polish) will optimize the wrong work. Read the components alongside: composite movement driven entirely by one dimension is a component story wearing a composite headline, and the trend needs its drivers named to be actionable.

## Formula

```
PQS = Weighted Index of Defects, Performance, Satisfaction
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** product_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 556 (batch 1)
