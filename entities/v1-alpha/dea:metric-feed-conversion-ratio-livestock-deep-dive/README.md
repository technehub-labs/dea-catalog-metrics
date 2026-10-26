# dea:metric-feed-conversion-ratio-livestock-deep-dive

Candidate Performance Metric record for **Feed Conversion Ratio - Livestock (Deep Dive)** (FCR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-feed-conversion-ratio-livestock-deep-dive`
- **Name:** Feed Conversion Ratio - Livestock (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FCR-D

## 2. Definition

Feed Conversion Ratio - Livestock (Deep Dive) (FCR-D) captures how efficiently resources are converted into outputs for organizations tracking agriculture & agronomy (deep dive). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Feed Consumed / Weight Gain - reported in ratio (x:1 or x). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Agriculture sector.

## 3. Context

Measures feed input per unit of animal output (weight gain, milk, eggs). It is the dominant economics of animal protein - feed is most of the cost - and the metric where genetics, health, and housing quality all surface. FCR improvements must be read against welfare and antibiotic-use constraints, since conversion optimized by aggressive growth regimens invites regulatory and consumer backlash. Read with herd health incidence and cost per tonne produced.

## Formula

```
Feed Consumed / Weight Gain
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** agriculture_agronomy_deep_dive
- **Sector:** agriculture

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2321 (batch 6)
