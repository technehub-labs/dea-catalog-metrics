# dea:metric-gig-worker-fulfilment-rate

Candidate Performance Metric record for **Gig Worker Fulfilment Rate** (GWFR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-gig-worker-fulfilment-rate`
- **Name:** Gig Worker Fulfilment Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** GWFR

## 2. Definition

Gig Worker Fulfilment Rate (GWFR) addresses the utilization or availability of capacity and is a fixture of gig & contingent workforce reporting. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Tasks Accepted within SLA / Tasks Posted - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Tasks Accepted within SLA / Tasks Posted
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** gig_contingent_workforce

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1460 (batch 5)
