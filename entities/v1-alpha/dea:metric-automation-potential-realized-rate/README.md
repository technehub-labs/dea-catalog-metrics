# dea:metric-automation-potential-realized-rate

Candidate Performance Metric record for **Automation Potential Realized Rate** (APRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-automation-potential-realized-rate`
- **Name:** Automation Potential Realized Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** APRR

## 2. Definition

Automation Potential Realized Rate (APRR) captures how efficiently resources are converted into outputs for organizations tracking operating model & process health deep dive. The formula is Automated Task Share of Automatable Tasks / Automatable - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how much of the assessed automatable work has actually been automated. Most organizations automate a fraction of what is technically possible. Realization measured by pilot rather than production deployment is potential, not realization. Read with process automation ratio (Deep Dive) and toil reduction rate.

## Formula

```
APRR = Automated Task Share of Automatable Tasks / Automatable
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** transformation
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** operating_model_process_health_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3502 (batch 7)
