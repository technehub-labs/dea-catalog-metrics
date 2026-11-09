# dea:metric-code-ownership-distribution-index

Candidate Performance Metric record for **Code Ownership Distribution Index** (CODI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-code-ownership-distribution-index`
- **Name:** Code Ownership Distribution Index
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CODI

## 2. Definition

A Software Development - Coding & Engineering Practices indicator, Code Ownership Distribution Index (CODI) quantifies exposure to adverse outcomes. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Files with Single Owner / Files, expressed in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## Formula

```
CODI = Files with Single Owner / Files
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** software_development_coding_engineering_practices

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2645 (batch 7)
