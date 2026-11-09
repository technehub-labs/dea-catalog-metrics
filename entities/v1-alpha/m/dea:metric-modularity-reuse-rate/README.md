# dea:metric-modularity-reuse-rate

Candidate Performance Metric record for **Modularity Reuse Rate** (MRR-SA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-modularity-reuse-rate`
- **Name:** Modularity Reuse Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MRR-SA

## 2. Definition

Modularity Reuse Rate (MRR-SA) addresses how efficiently resources are converted into outputs and is a fixture of software architecture & technical design reporting. It is defined as Shared Component Usage / Total Component Usage; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of functionality delivered through reused modules and services rather than newly built equivalents. It is the leverage metric of software economics: reuse concentrates maintenance, accelerates delivery, and enforces consistency, and low rates indicate siloed teams rebuilding what exists. Reuse must be measured against actual adoption, not module availability - existing-but-ignored modules are organizational debt. Read with design reuse patterns across teams and duplication-detection scans.

## Formula

```
MRR-SA = Shared Component Usage / Total Component Usage
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** software_architecture_technical_design

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2625 (batch 7)
