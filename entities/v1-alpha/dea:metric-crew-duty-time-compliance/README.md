# dea:metric-crew-duty-time-compliance

Candidate Performance Metric record for **Crew Duty Time Compliance** (CDTC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-crew-duty-time-compliance`
- **Name:** Crew Duty Time Compliance
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CDTC

## 2. Definition

Crew Duty Time Compliance (CDTC) addresses conformance to standards, plans, or obligations and is a fixture of airlines & aviation reporting. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Crew Rosters within Duty Limits / Rosters Checked - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Airlines & aviation sector.

## Formula

```
Crew Rosters within Duty Limits / Rosters Checked
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 661 (batch 2)
