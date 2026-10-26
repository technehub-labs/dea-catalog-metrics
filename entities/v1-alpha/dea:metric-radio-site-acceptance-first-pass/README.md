# dea:metric-radio-site-acceptance-first-pass

Candidate Performance Metric record for **Radio Site Acceptance First Pass** (RSAF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-radio-site-acceptance-first-pass`
- **Name:** Radio Site Acceptance First Pass
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RSAF

## 2. Definition

Radio Site Acceptance First Pass (RSAF) addresses the quality of outputs and outcomes and is a fixture of telecom field & installation reporting. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Sites Accepted on First Inspection / Sites Inspected, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Telecommunications.

## 3. Context

Measures the share of built network sites passing acceptance testing first time. It matters because failed acceptance delays revenue-generating coverage and doubles installation cost. Acceptance criteria can be softened under rollout pressure to keep schedules. Read with Post-Acceptance Fault Rate and Rework cost to confirm first-pass sites are genuinely sound.

## Formula

```
Sites Accepted on First Inspection / Sites Inspected
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** telecom_field_installation
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1286 (batch 5)
