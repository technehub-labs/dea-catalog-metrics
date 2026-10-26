# dea:metric-patch-to-deploy-lag-dependencies

Candidate Performance Metric record for **Patch-to-Deploy Lag (Dependencies)** (PTDL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-patch-to-deploy-lag-dependencies`
- **Name:** Patch-to-Deploy Lag (Dependencies)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PTDL

## 2. Definition

Patch-to-Deploy Lag (Dependencies) (PTDL) addresses exposure to adverse outcomes and is a fixture of application security (appsec) reporting. It is computed as Days from Patch Release to Dependency Deployed, expressed in days. Its use is concentrated in Software. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Days from Patch Release to Dependency Deployed
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** application_security_appsec
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3332 (batch 7)
