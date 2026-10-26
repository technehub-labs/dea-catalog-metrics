# dea:metric-technical-dispatch-reliability

Candidate Performance Metric record for **Technical Dispatch Reliability** (TDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-technical-dispatch-reliability`
- **Name:** Technical Dispatch Reliability
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TDR

## 2. Definition

Technical Dispatch Reliability (TDR) captures the quality of outputs and outcomes for organizations tracking airlines & aviation. The formula is Departures without Technical Delay or Cancellation / Total Departures - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Airlines & aviation sector.

## Formula

```
Departures without Technical Delay or Cancellation / Total Departures
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airlines_aviation
- **Sector:** airlines_aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 654 (batch 2)
