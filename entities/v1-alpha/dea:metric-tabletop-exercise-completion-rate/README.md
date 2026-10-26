# dea:metric-tabletop-exercise-completion-rate

Candidate Performance Metric record for **Tabletop Exercise Completion Rate** (TECR-SOC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-tabletop-exercise-completion-rate`
- **Name:** Tabletop Exercise Completion Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** TECR-SOC

## 2. Definition

Tabletop Exercise Completion Rate (TECR-SOC) addresses capability maturity or development and is a fixture of secops & security operations center reporting. Its calculation is Exercises Completed per Year / Planned, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of required incident-response exercises conducted on schedule. Tabletops expose plan-versus-reality gaps before an attacker does. Exercises without executive participation and injected realism test little. Read with purple team exercise improvement rate and mean time to respond - security.

## Formula

```
Exercises Completed per Year / Planned
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** secops_security_operations_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2791 (batch 7)
