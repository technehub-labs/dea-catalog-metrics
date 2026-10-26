# dea:metric-ridership-growth-rate

Candidate Performance Metric record for **Ridership Growth Rate** (RGR-T) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ridership-growth-rate`
- **Name:** Ridership Growth Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RGR-T

## 2. Definition

Within Public Transit, Ridership Growth Rate (RGR-T) is used to gauge growth over time. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is (Ridership_current - Ridership_prior) / Ridership_prior - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Public transit sector.

## 3. Context

Ridership growth measures the change in passenger trips, and it is the transit metric that determines system economics at scale - most costs are fixed, so additional riders arrive at near-zero marginal cost while fare revenue grows. The post-pandemic ridership collapse and partial recovery showed how fragile the metric is to external shocks (remote work, safety perception, fare policy). Growth decomposition matters: population growth, service expansion (new routes add trips mechanically), mode shift, and real per-capita usage growth are distinct drivers with different strategic meaning. Read with farebox recovery (growth heals subsidy economics), service reliability (unreliable service suppresses ridership growth even when demand exists), and remote-work structural shifts in commute patterns.

## Formula

```
(Ridership_current - Ridership_prior) / Ridership_prior
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** public_transit
- **Sector:** public_transit

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1009 (batch 3)
