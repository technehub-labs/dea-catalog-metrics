# dea:metric-management-action-closure-rate

Candidate Performance Metric record for **Management Action Closure Rate** (MACR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-management-action-closure-rate`
- **Name:** Management Action Closure Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MACR

## 2. Definition

A Internal Audit indicator, Management Action Closure Rate (MACR) quantifies conformance to standards, plans, or obligations. It is computed as Actions Closed by Due Date / Actions Due, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of agreed audit management actions closed on time. It matters because unclosed actions are accepted risks compounding in silence. Closures can be administrative, with the underlying control still unremediated. Read with Overdue Management Actions and repeat-finding rates to confirm closure means remediation.

## Formula

```
MACR = Actions Closed by Due Date / Actions Due
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** internal_audit

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 615 (batch 2)
