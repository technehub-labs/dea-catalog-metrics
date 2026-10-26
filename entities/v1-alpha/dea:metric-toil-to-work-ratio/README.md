# dea:metric-toil-to-work-ratio

Candidate Performance Metric record for **Toil-to-Work Ratio** (T2WR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-toil-to-work-ratio`
- **Name:** Toil-to-Work Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** T2WR

## 2. Definition

Within Observability & Site Reliability Engineering, Toil-to-Work Ratio (T2WR) is used to gauge how efficiently resources are converted into outputs. The formula is Toil Hours / Total Engineering Hours - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures operational toil as a share of total engineering effort. Above roughly 30%, teams are firefighting rather than improving, and attrition follows. Self-reported toil categorization is inconsistent; baselines matter more than precision. Read with toil reduction rate and SRE reliability review coverage.

## Formula

```
T2WR = Toil Hours / Total Engineering Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** observability_site_reliability_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2876 (batch 7)
