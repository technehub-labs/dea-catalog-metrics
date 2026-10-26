# dea:metric-incident-caused-by-change-rate

Candidate Performance Metric record for **Incident Caused by Change Rate** (ICBCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-incident-caused-by-change-rate`
- **Name:** Incident Caused by Change Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ICBCR

## 2. Definition

Within IT Incident & Major Problem Management, Incident Caused by Change Rate (ICBCR) is used to gauge exposure to adverse outcomes. It is computed as Incidents Caused by Recent Change / Incidents, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of incidents traced to changes (deployments, config, infrastructure). Change-induced incidents are self-inflicted and therefore preventable. The rate rises with honest attribution, so a suspiciously low number can mean blame-avoiding classification. Read with change failure rate and release incident rate.

## Formula

```
Incidents Caused by Recent Change / Incidents
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** it_incident_major_problem_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2895 (batch 7)
