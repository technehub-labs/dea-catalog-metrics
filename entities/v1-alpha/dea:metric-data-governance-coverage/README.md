# dea:metric-data-governance-coverage

Candidate Performance Metric record for **Data Governance Coverage** (DGC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-governance-coverage`
- **Name:** Data Governance Coverage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DGC

## 2. Definition

Within Data Management & Analytics, Data Governance Coverage (DGC) is used to gauge conformance to standards, plans, or obligations. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Data Domains with Steward and Standards / Total Domains; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The share of critical data assets with defined ownership, stewardship, classification, and quality rules - the organizational metric that measures whether governance exists in practice rather than in a policy deck. Its strategic weight is regulatory and analytic simultaneously: privacy regimes demand knowing where personal data lives and who answers for it, and analytic programs demand trusted definitions of shared metrics - the single version of the truth that only governance coverage actually delivers. The metric is honest only when defined against a critical-data inventory, since governing every table is impossible and governing nothing is negligence, and the inventory exercise is where most of the value hides. Read with the index of governance quality: coverage with named but unresponsive owners is administrative decoration, which is why stewards need escalation paths that actually fire.

## Formula

```
Data Domains with Steward and Standards / Total Domains
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** data_management_analytics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 344 (batch 1)
