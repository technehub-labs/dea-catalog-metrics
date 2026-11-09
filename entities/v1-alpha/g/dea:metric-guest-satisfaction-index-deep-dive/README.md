# dea:metric-guest-satisfaction-index-deep-dive

Candidate Performance Metric record for **Guest Satisfaction Index (Deep Dive)** (GSI-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-guest-satisfaction-index-deep-dive`
- **Name:** Guest Satisfaction Index (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** GSI-D

## 2. Definition

Guest Satisfaction Index (Deep Dive) (GSI-D) addresses the engagement or satisfaction of the people involved and is a fixture of hotel & resort operations (deep dive) reporting. The formula is Composite Guest Survey Score - reported in index (0-100 or normalized). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Hospitality sector.

## 3. Context

Measures aggregated guest satisfaction across the stay journey. In hotels, satisfaction drives review scores, which drive ranking, which drives organic booking share - a compounding loop where experience becomes distribution economics. Post-stay surveys suffer response bias, so triangulate with review-text sentiment and complaint data. Read with online reputation score (Hotels) and repeat-stay rates.

## Formula

```
GSI-D = Composite Guest Survey Score
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** engagement
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** hotel_resort_operations_deep_dive
- **Sector:** hospitality

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1906 (batch 6)
