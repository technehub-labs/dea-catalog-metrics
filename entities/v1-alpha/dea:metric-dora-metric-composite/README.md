# dea:metric-dora-metric-composite

Candidate Performance Metric record for **DORA Metric Composite** (DORA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-dora-metric-composite`
- **Name:** DORA Metric Composite
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DORA

## 2. Definition

Within Software Engineering, DORA Metric Composite (DORA) is used to gauge how effectively a process or entity achieves its intended outcome. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Index of Deployment Frequency, Lead Time, Change Failure, MTTRS, measured in index (0-100 or normalized). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The four delivery metrics of the DevOps Research and Assessment program - deployment frequency, lead time for changes, change failure rate, and time to restore service - combined into a single performance score. The composite exists because the four are a system: throughput without stability is chaos, stability without throughput is stagnation, and the research tradition behind the program found elite performers deliver both extremes simultaneously, which composite scoring rewards and single-metric tracking does not. Its strategic use is benchmarking: the annual State of DevOps reports publish performance bands that let an organization locate itself against industry, and the gap to the elite band is a roadmap. The honest composite needs consistent measurement definitions across teams, since each metric is trivially gameable alone.

## Formula

```
Index of Deployment Frequency, Lead Time, Change Failure, MTTRS
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** software_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 295 (batch 1)
