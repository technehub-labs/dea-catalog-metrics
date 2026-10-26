# dea:metric-upgrade-project-slippage-rate

Candidate Performance Metric record for **Upgrade Project Slippage Rate** (UPSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-upgrade-project-slippage-rate`
- **Name:** Upgrade Project Slippage Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** UPSR

## 2. Definition

Upgrade Project Slippage Rate (UPSR) measures exposure to adverse outcomes in the ERP & Enterprise Application Operations domain. It is computed as Schedule Slippage / Planned Duration, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Schedule Slippage / Planned Duration
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** erp_enterprise_application_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2178 (batch 6)
