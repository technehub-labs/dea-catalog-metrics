# dea:metric-journal-entry-control-exception-rate

Candidate Performance Metric record for **Journal Entry Control Exception Rate** (JECE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-journal-entry-control-exception-rate`
- **Name:** Journal Entry Control Exception Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** JECE

## 2. Definition

Journal Entry Control Exception Rate (JECE) captures exposure to adverse outcomes for organizations tracking internal controls & financial reporting integrity. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Manual Journal Entries Breaching Control / Manual Entries - reported in events per thousand or million (scaled). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Manual Journal Entries Breaching Control / Manual Entries
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** internal_controls_financial_reporting_integrity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3580 (batch 8)
