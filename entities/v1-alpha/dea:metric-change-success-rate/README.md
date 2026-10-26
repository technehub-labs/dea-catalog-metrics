# dea:metric-change-success-rate

Candidate Performance Metric record for **Change Success Rate** (ChSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-change-success-rate`
- **Name:** Change Success Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ChSR

## 2. Definition

A IT Service Management indicator, Change Success Rate (ChSR) quantifies the quality of outputs and outcomes. Its calculation is Successful Changes / Total Changes, measured in percent (%). It is applied across virtually every sector. Its value drives prioritization and resource reallocation among competing initiatives. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of changes implemented without incident, rollback, or breach. It matters because change is the dominant cause of outages, so this is the core stability lever. Gaming risk includes excluding emergency fixes from the denominator or rolling back quietly outside the record. Read with Emergency Change Rate and Change Failure Recovery Time to judge whether green changes are truly low-risk.

## Formula

```
ChSR = Successful Changes / Total Changes
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** it_service_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 305 (batch 1)
