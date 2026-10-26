# dea:metric-observability-onboarding-time-new-service

Candidate Performance Metric record for **Observability Onboarding Time (New Service)** (OONT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-observability-onboarding-time-new-service`
- **Name:** Observability Onboarding Time (New Service)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** OONT

## 2. Definition

Observability Onboarding Time (New Service) (OONT) measures how efficiently resources are converted into outputs in the SRE & Observability Standard Measures domain. The formula is Days from Service Launch to Full Instrumentation - reported in days. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Lower values are better; each reduction is an improvement. It is a standard measure in the Software sector.

## Formula

```
Days from Service Launch to Full Instrumentation
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sre_observability_standard_measures
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4391 (batch 11)
