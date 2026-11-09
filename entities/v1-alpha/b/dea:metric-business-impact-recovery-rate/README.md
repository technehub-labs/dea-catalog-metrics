# dea:metric-business-impact-recovery-rate

Candidate Performance Metric record for **Business Impact Recovery Rate** (BIRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-business-impact-recovery-rate`
- **Name:** Business Impact Recovery Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BIRR

## 2. Definition

Business Impact Recovery Rate (BIRR) measures how effectively a process or entity achieves its intended outcome in the IT Incident & Major Problem Management domain. Its calculation is Transactions Recovered after Rerouting or Failover / Affected, measured in percent (%). It is applied across virtually every sector. Its value drives prioritization and resource reallocation among competing initiatives. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
BIRR = Transactions Recovered after Rerouting or Failover / Affected
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** it_incident_major_problem_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2902 (batch 7)
