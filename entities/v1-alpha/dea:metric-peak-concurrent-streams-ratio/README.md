# dea:metric-peak-concurrent-streams-ratio

Candidate Performance Metric record for **Peak Concurrent Streams Ratio** (PCSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-peak-concurrent-streams-ratio`
- **Name:** Peak Concurrent Streams Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PCSR

## 2. Definition

Peak Concurrent Streams Ratio (PCSR) captures the utilization or availability of capacity for organizations tracking broadcasting & streaming media. It is computed as Peak Concurrent Streams / Design Capacity, expressed in percent (%). Its use is concentrated in Media & Entertainment. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Values outside the intended band, on either side, warrant investigation.

## Formula

```
Peak Concurrent Streams / Design Capacity
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** broadcasting_streaming_media
- **Sector:** media_entertainment

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1961 (batch 6)
