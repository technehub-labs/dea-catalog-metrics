# dea:metric-attraction-downtime-ratio

Candidate Performance Metric record for **Attraction Downtime Ratio** (ADR-V) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-attraction-downtime-ratio`
- **Name:** Attraction Downtime Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ADR-V

## 2. Definition

Attraction Downtime Ratio (ADR-V) measures the utilization or availability of capacity in the Entertainment Venues & Attractions domain. The formula is Ride or Exhibit Downtime / Operating Hours - reported in percent (%). It is a standard measure in the Media & Entertainment sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
ADR-V = Ride or Exhibit Downtime / Operating Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** entertainment_venues_attractions
- **Sector:** media_entertainment

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1946 (batch 6)
