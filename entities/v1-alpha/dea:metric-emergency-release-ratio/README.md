# dea:metric-emergency-release-ratio

Candidate Performance Metric record for **Emergency Release Ratio** (ERR-RM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-emergency-release-ratio`
- **Name:** Emergency Release Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ERR-RM

## 2. Definition

A Release Management & Environments indicator, Emergency Release Ratio (ERR-RM) quantifies exposure to adverse outcomes. The formula is Emergency Releases / Total Releases - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the share of production changes pushed through emergency, bypass-governance paths. A rising ratio signals that normal release processes are too slow or too rigid, and that urgency has become a habit. Some emergency changes are legitimate; the metric punishes the pipeline, not the people. Read with release cycle time and security gate enforcement rate.

## Formula

```
Emergency Releases / Total Releases
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** release_management_environments

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2746 (batch 7)
