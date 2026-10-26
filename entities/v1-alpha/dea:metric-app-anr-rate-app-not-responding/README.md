# dea:metric-app-anr-rate-app-not-responding

Candidate Performance Metric record for **App ANR Rate (App Not Responding)** (ANRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-app-anr-rate-app-not-responding`
- **Name:** App ANR Rate (App Not Responding)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ANRR

## 2. Definition

App ANR Rate (App Not Responding) (ANRR) captures the quality of outputs and outcomes for organizations tracking mobile & client development. It is computed as ANR Events / Sessions, expressed in events per thousand or million (scaled). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Lower values are better; each reduction is an improvement. Its use is concentrated in Software.

## Formula

```
ANR Events / Sessions
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** mobile_client_development
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3253 (batch 7)
