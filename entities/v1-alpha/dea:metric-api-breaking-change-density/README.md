# dea:metric-api-breaking-change-density

Candidate Performance Metric record for **API Breaking Change Density** (APBCD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-api-breaking-change-density`
- **Name:** API Breaking Change Density
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** APBCD

## 2. Definition

Within Code Quality & Static Analysis, API Breaking Change Density (APBCD) is used to gauge exposure to adverse outcomes. The formula is Breaking Changes per Major Release - reported in ratio (x:1 or x). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Lower values are better; each reduction is an improvement. It is a standard measure in the Software sector.

## Formula

```
Breaking Changes per Major Release
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** code_quality_static_analysis
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4192 (batch 9)
