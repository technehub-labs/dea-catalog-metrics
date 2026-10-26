# dea:metric-esg-rating-score

Candidate Performance Metric record for **ESG Rating Score** (ESGR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-esg-rating-score`
- **Name:** ESG Rating Score
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ESGR

## 2. Definition

ESG Rating Score (ESGR) measures conformance to standards, plans, or obligations in the Sustainability & ESG domain. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Composite Rating from Recognized ESG Rater, expressed in score (points). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

A composite third-party assessment of environmental, social, and governance performance - the metric that condenses a whole sustainability program into one letter or number for investors who cannot parse raw disclosures. Its strategic weight is capital-market access: portfolio mandates, index inclusion, and some lenders price against these scores, so a downgrade has real financing consequence. The known problem is divergence: correlation between major raters is famously far from perfect, and the same company can be a leader in one methodology and a laggard in another, because weightings and materiality choices differ - so managing the score requires knowing which methodology matters to your capital providers and engaging that one directly. Read the underlying pillars separately: governance tends to dominate the financial-materiality models more than intuition suggests, and environmental scores move on targets and disclosure as much as on physical performance.

## Formula

```
Composite Rating from Recognized ESG Rater
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** sustainability_esg

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 425 (batch 1)
