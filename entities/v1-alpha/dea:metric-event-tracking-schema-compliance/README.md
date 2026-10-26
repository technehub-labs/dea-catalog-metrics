# dea:metric-event-tracking-schema-compliance

Candidate Performance Metric record for **Event Tracking Schema Compliance** (ETSC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-event-tracking-schema-compliance`
- **Name:** Event Tracking Schema Compliance
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ETSC

## 2. Definition

Event Tracking Schema Compliance (ETSC) captures conformance to standards, plans, or obligations for organizations tracking web & digital analytics standard measures. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Tracked Events Matching Governance Schema / Events - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Digital product sector.

## Formula

```
Tracked Events Matching Governance Schema / Events
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** web_digital_analytics_standard_measures
- **Sector:** digital_product

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4366 (batch 11)
