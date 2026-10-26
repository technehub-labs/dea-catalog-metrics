# dea:metric-live-sports-uptime-streaming

Candidate Performance Metric record for **Live Sports Uptime (Streaming)** (LSUS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-live-sports-uptime-streaming`
- **Name:** Live Sports Uptime (Streaming)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** LSUS

## 2. Definition

Live Sports Uptime (Streaming) (LSUS) measures the utilization or availability of capacity in the Broadcasting & Streaming Media domain. It is defined as Live Stream Uptime during Events / Event Hours; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. In Media & Entertainment, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the availability and quality of live sports streams during events. Live sports is the highest-stakes streaming workload - subscriber tolerance for buffering during a match is near zero, and outage events drive immediate cancel spikes and social backlash. Measure during-peak concurrent load, not average availability, and by market and device. Read with incident root causes, CDN capacity headroom, and churn around outage events.

## Formula

```
LSUS = Live Stream Uptime during Events / Event Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1967 (batch 6)
