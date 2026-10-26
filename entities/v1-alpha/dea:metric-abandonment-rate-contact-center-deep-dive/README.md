# dea:metric-abandonment-rate-contact-center-deep-dive

Candidate Performance Metric record for **Abandonment Rate (Contact Center Deep Dive)** (ABDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-abandonment-rate-contact-center-deep-dive`
- **Name:** Abandonment Rate (Contact Center Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ABDD

## 2. Definition

Abandonment Rate (Contact Center Deep Dive) (ABDD) addresses the quality of outputs and outcomes and is a fixture of contact center standard measures (deep dive) reporting. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Callers Abandoning before Answer / Calls Offered - reported in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Callers Abandoning before Answer / Calls Offered
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contact_center_standard_measures_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4318 (batch 10)
