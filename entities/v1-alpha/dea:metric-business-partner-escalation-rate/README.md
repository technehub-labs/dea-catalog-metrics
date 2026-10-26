# dea:metric-business-partner-escalation-rate

Candidate Performance Metric record for **Business Partner Escalation Rate** (BPER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-business-partner-escalation-rate`
- **Name:** Business Partner Escalation Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BPER

## 2. Definition

Business Partner Escalation Rate (BPER) addresses the quality of outputs and outcomes and is a fixture of shared services & global business services reporting. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Escalations to Business Partner / Total Requests - reported in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
BPER = Escalations to Business Partner / Total Requests
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** shared_services_global_business_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1063 (batch 4)
