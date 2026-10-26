# dea:metric-security-awareness-training-completion

Candidate Performance Metric record for **Security Awareness Training Completion** (SATC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-security-awareness-training-completion`
- **Name:** Security Awareness Training Completion
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SATC

## 2. Definition

Security Awareness Training Completion (SATC) measures conformance to standards, plans, or obligations in the Cybersecurity domain. The formula is Users Completing Training / Users Assigned - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
SATC = Users Completing Training / Users Assigned
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** cybersecurity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 324 (batch 1)
