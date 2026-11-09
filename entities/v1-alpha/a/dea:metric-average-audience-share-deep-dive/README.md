# dea:metric-average-audience-share-deep-dive

Candidate Performance Metric record for **Average Audience Share (Deep Dive)** (AAS-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-audience-share-deep-dive`
- **Name:** Average Audience Share (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** AAS-D

## 2. Definition

Average Audience Share (Deep Dive) (AAS-D) measures growth over time in the Broadcasting & Streaming Media domain. The formula is Viewers of Channel / Total Viewers - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Media & Entertainment sector.

## 3. Context

Measures the audience watching a channel or program as a share of the total viewing universe in its slot. It is the pricing currency of broadcast advertising, and share trends reveal scheduling and content strategy failures faster than absolute reach. Cross-platform measurement fragmentation (linear versus streaming) increasingly distorts the denominator, so demand consistent measurement windows. Read with streaming churn rate (Deep Dive) for the structural audience migration.

## Formula

```
AAS-D = Viewers of Channel / Total Viewers
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** broadcasting_streaming_media
- **Sector:** media_entertainment

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1955 (batch 6)
