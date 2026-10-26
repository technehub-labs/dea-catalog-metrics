# dea:metric-service-scalability-headroom

Candidate Performance Metric record for **Service Scalability Headroom** (SSH-SA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-service-scalability-headroom`
- **Name:** Service Scalability Headroom
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SSH-SA

## 2. Definition

A Software Architecture & Technical Design indicator, Service Scalability Headroom (SSH-SA) quantifies the utilization or availability of capacity. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Peak Load / Designed Capacity - reported in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the capacity buffer between current load and system limits at peak. Headroom is the incident-prevention metric for growth: services without buffer fail on the viral hour or the seasonal peak, and the metric forces capacity honesty ahead of the capacity plan. Headroom must be measured at the constraint (the service that saturates first), since system headroom is only as real as its tightest component. Read with load-test currency and peak-season incident history.

## Formula

```
Peak Load / Designed Capacity
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** software_architecture_technical_design

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2630 (batch 7)
