# dea:metric-incident-free-release-rate-deep-dive

Candidate Performance Metric record for **Incident-Free Release Rate (Deep Dive)** (IFRRD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-incident-free-release-rate-deep-dive`
- **Name:** Incident-Free Release Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** IFRRD

## 2. Definition

Incident-Free Release Rate (Deep Dive) (IFRRD) captures the quality of outputs and outcomes for organizations tracking sre & observability standard measures. The formula is Releases without Error Budget Impact / Releases - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Software sector.

## Formula

```
Releases without Error Budget Impact / Releases
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sre_observability_standard_measures
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4385 (batch 11)
