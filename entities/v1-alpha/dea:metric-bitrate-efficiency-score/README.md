# dea:metric-bitrate-efficiency-score

Candidate Performance Metric record for **Bitrate Efficiency Score** (BES) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-bitrate-efficiency-score`
- **Name:** Bitrate Efficiency Score
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BES

## 2. Definition

Within Broadcasting & Streaming Media, Bitrate Efficiency Score (BES) is used to gauge the quality of outputs and outcomes. It is computed as Perceived Quality per Bitrate Delivered, expressed in index (0-100 or normalized). Its use is concentrated in Media & Entertainment. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
BES = Perceived Quality per Bitrate Delivered
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
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** broadcasting_streaming_media
- **Sector:** media_entertainment

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1964 (batch 6)
