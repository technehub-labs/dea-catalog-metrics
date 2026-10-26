# dea:metric-quality-of-experience-score-video-streaming

Candidate Performance Metric record for **Quality of Experience Score (Video Streaming)** (QoE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-quality-of-experience-score-video-streaming`
- **Name:** Quality of Experience Score (Video Streaming)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** QoE

## 2. Definition

Quality of Experience Score (Video Streaming) (QoE) measures the quality of outputs and outcomes in the Telecom Product & Bundle Management domain. It is defined as Weighted Index of Start Time, Rebuffering, Resolution; the result is stated in index (0-100 or normalized). In Telecommunications, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures technical delivery quality of streaming - start-up time, rebuffering ratio, bitrate stability - as perceived by customers. In streaming, experience quality is retention: rebuffering directly predicts cancels. Measurement must be device and network segmented, since averages hide the worst-experience cohorts most likely to churn. Read with complaint and churn patterns by stream quality tier and network type.

## Formula

```
Weighted Index of Start Time, Rebuffering, Resolution
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
- **Domain:** telecom_product_bundle_management
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1448 (batch 5)
