# dea:metric-handover-success-rate

Candidate Performance Metric record for **Handover Success Rate** (HOSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-handover-success-rate`
- **Name:** Handover Success Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** HOSR

## 2. Definition

Handover Success Rate (HOSR) addresses the quality of outputs and outcomes and is a fixture of telecom network operations reporting. It is computed as Successful Handovers / Handover Attempts, expressed in percent (%). Its use is concentrated in Telecommunications. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Successful Handovers / Handover Attempts
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
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** telecom_network_operations
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 862 (batch 3)
