# dea:metric-cross-team-dependency-lead-time

Candidate Performance Metric record for **Cross-Team Dependency Lead Time** (CTDLT-AG) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cross-team-dependency-lead-time`
- **Name:** Cross-Team Dependency Lead Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CTDLT-AG

## 2. Definition

Cross-Team Dependency Lead Time (CTDLT-AG) captures how efficiently resources are converted into outputs for organizations tracking agile delivery & team effectiveness. It is computed as Days Waiting on External Team Dependencies, expressed in days. It is reviewed at cadence by planning owners to correct course before issues become strategic. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
CTDLT-AG = Days Waiting on External Team Dependencies
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** organization
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** agile_delivery_team_effectiveness

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2987 (batch 7)
