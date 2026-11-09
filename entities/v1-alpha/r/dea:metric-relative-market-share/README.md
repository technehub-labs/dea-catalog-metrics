# dea:metric-relative-market-share

Candidate Performance Metric record for **Relative Market Share** (RMS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-relative-market-share`
- **Name:** Relative Market Share
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RMS

## 2. Definition

Relative Market Share (RMS) measures growth over time in the Market Structure & Economics Standard Measures domain. The formula is Entity Market Share / Largest Competitor Share - reported in ratio (x:1 or x). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the company's share relative to its largest competitor. Relative share is the classic BCG input: it correlates with cost position and cash generation. Leader-versus-follower comparisons mislead in fragmented markets. Read with market share (Deep Dive) and four-firm concentration ratio.

## Formula

```
RMS = Entity Market Share / Largest Competitor Share
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** growth
- **Scope classification:** business_domain
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** market_structure_economics_standard_measures

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4137 (batch 9)
