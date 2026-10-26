# dea:metric-schedule-variance-in-construction

Candidate Performance Metric record for **Schedule Variance in Construction** (SV-C) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-schedule-variance-in-construction`
- **Name:** Schedule Variance in Construction
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SV-C

## 2. Definition

Schedule Variance in Construction (SV-C) captures conformance to standards, plans, or obligations for organizations tracking construction & engineering. It is computed as (Earned Work - Planned Work) / Planned Work, expressed in percent (%). Its use is concentrated in Construction & engineering. It is reviewed at cadence by planning owners to correct course before issues become strategic. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures deviation of actual progress from the baseline schedule. It matters because delay is the primary driver of construction cost overruns and disputes. Teams can hide variance by re-baselining or by measuring progress via subjective percent-complete. Read with Cost Variance in Construction and Milestone Adherence to detect baseline games versus real slippage.

## Formula

```
(Earned Work - Planned Work) / Planned Work
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** construction_engineering
- **Sector:** construction_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 662 (batch 2)
