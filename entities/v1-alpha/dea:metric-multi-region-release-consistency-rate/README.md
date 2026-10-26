# dea:metric-multi-region-release-consistency-rate

Candidate Performance Metric record for **Multi-Region Release Consistency Rate** (MRRCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-multi-region-release-consistency-rate`
- **Name:** Multi-Region Release Consistency Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MRRCR

## 2. Definition

Multi-Region Release Consistency Rate (MRRCR) addresses the quality of outputs and outcomes and is a fixture of release management & environments reporting. Its calculation is Regions Deployed within Alignment Window / Regions, measured in percent (%). Its value drives prioritization and resource reallocation among competing initiatives. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Regions Deployed within Alignment Window / Regions
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
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** release_management_environments

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2744 (batch 7)
