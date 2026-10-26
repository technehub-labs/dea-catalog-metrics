# dea:metric-schedule-variance-percent-deep-dive

Candidate Performance Metric record for **Schedule Variance Percent (Deep Dive)** (SVP-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-schedule-variance-percent-deep-dive`
- **Name:** Schedule Variance Percent (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SVP-D

## 2. Definition

Schedule Variance Percent (Deep Dive) (SVP-D) addresses conformance to standards, plans, or obligations and is a fixture of project management (deep dive) reporting. It is defined as (Actual Duration - Baseline Duration) / Baseline Duration; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how far actual project progress deviates from the baseline schedule. Schedule variance is the earliest leading indicator of delivery trouble. Managers mask variance via re-baselining rather than recovery. Read with estimate accuracy - schedule and milestone hit rate.

## Formula

```
(Actual Duration - Baseline Duration) / Baseline Duration
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** project_management_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2929 (batch 7)
