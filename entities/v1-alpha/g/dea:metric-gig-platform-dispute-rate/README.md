# dea:metric-gig-platform-dispute-rate

Candidate Performance Metric record for **Gig Platform Dispute Rate** (GPDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-gig-platform-dispute-rate`
- **Name:** Gig Platform Dispute Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** GPDR

## 2. Definition

Gig Platform Dispute Rate (GPDR) addresses exposure to adverse outcomes and is a fixture of gig & contingent workforce reporting. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Disputed Tasks / Tasks Completed, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
GPDR = Disputed Tasks / Tasks Completed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** gig_contingent_workforce

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1467 (batch 5)
