# dea:metric-original-content-roi-streaming

Candidate Performance Metric record for **Original Content ROI (Streaming)** (OCR-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-original-content-roi-streaming`
- **Name:** Original Content ROI (Streaming)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** OCR-S

## 2. Definition

Original Content ROI (Streaming) (OCR-S) measures the economic value created or preserved in the Broadcasting & Streaming Media domain. Its calculation is Attributed Subscriber Value / Content Cost, measured in ratio (x:1 or x). It originates from and is most used in Media & Entertainment practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures returns on original content investment - retention, acquisition, and engagement value against production and marketing cost. Content ROI is genuinely hard: attribution of subscriber decisions to titles requires churn modeling with holdouts, and studios that skip this fly blind on billion-dollar budgets. Read both direct (title-driven signups) and indirect (engagement lift) value. Read with content hours share of viewing and churn model lift by title window.

## Formula

```
OCR-S = Attributed Subscriber Value / Content Cost
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** value_delivery
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1963 (batch 6)
