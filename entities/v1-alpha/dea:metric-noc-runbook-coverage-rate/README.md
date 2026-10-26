# dea:metric-noc-runbook-coverage-rate

Candidate Performance Metric record for **NOC Runbook Coverage Rate** (NRCR-NOC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-noc-runbook-coverage-rate`
- **Name:** NOC Runbook Coverage Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** NRCR-NOC

## 2. Definition

NOC Runbook Coverage Rate (NRCR-NOC) addresses capability maturity or development and is a fixture of network operations center (deep dive) reporting. It is computed as Alert Types with Runbooks / Alert Types, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Alert Types with Runbooks / Alert Types
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** network_operations_center_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2850 (batch 7)
