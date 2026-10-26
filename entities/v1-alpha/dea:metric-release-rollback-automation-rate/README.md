# dea:metric-release-rollback-automation-rate

Candidate Performance Metric record for **Release Rollback Automation Rate** (RRA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-release-rollback-automation-rate`
- **Name:** Release Rollback Automation Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RRA

## 2. Definition

Release Rollback Automation Rate (RRA) captures how efficiently resources are converted into outputs for organizations tracking sre & observability standard measures. It is computed as Rollbacks Executed via Automated Path / Rollbacks, expressed in percent (%). Its use is concentrated in Software. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Rollbacks Executed via Automated Path / Rollbacks
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sre_observability_standard_measures
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4388 (batch 11)
