# dea:metric-voice-of-customer-coverage

Candidate Performance Metric record for **Voice of Customer Coverage** (VOCC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-voice-of-customer-coverage`
- **Name:** Voice of Customer Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** VOCC

## 2. Definition

Voice of Customer Coverage (VOCC) captures how effectively a process or entity achieves its intended outcome for organizations tracking requirements engineering & product discovery. The formula is Features Informed by VOC Evidence / Features Delivered - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of product decisions and discovery work incorporating direct customer input. It is the demand-side grounding of product development: coverage prevents the build-what-we-assume failure pattern, and it is measured across discovery, prioritization, and validation stages. Coverage must include detractors and churned users, since current-customer panels are survivorship bias in survey form. Read with customer segment NPS trends and discovery evidence in roadmap reviews.

## Formula

```
Features Informed by VOC Evidence / Features Delivered
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
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** requirements_engineering_product_discovery

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2616 (batch 7)
