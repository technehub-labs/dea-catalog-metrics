# dea:metric-guard-tour-completion

Candidate Performance Metric record for **Guard Tour Completion** (GTC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-guard-tour-completion`
- **Name:** Guard Tour Completion
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** GTC

## 2. Definition

Guard Tour Completion (GTC) addresses conformance to standards, plans, or obligations and is a fixture of physical security operations reporting. It provides the day-to-day signal that a process is running as designed. Its calculation is Patrol Tours Completed / Tours Scheduled, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
GTC = Patrol Tours Completed / Tours Scheduled
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** physical_security_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1209 (batch 4)
