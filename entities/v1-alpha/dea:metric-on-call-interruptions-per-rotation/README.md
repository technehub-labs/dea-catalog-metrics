# dea:metric-on-call-interruptions-per-rotation

Candidate Performance Metric record for **On-Call Interruptions per Rotation** (OCIPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-on-call-interruptions-per-rotation`
- **Name:** On-Call Interruptions per Rotation
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** OCIPR

## 2. Definition

A Observability & Site Reliability Engineering indicator, On-Call Interruptions per Rotation (OCIPR) quantifies the engagement or satisfaction of the people involved. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Pages per On-Call Rotation Week - reported in count (items per period). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Pages per On-Call Rotation Week
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** engagement
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** observability_site_reliability_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2870 (batch 7)
