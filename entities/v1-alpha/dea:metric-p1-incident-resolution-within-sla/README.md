# dea:metric-p1-incident-resolution-within-sla

Candidate Performance Metric record for **P1 Incident Resolution within SLA** (P1IRSLA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-p1-incident-resolution-within-sla`
- **Name:** P1 Incident Resolution within SLA
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** P1IRSLA

## 2. Definition

Within IT Incident & Major Problem Management, P1 Incident Resolution within SLA (P1IRSLA) is used to gauge conformance to standards, plans, or obligations. It is defined as P1 Incidents Resolved within SLA / P1 Incidents; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of highest-severity incidents resolved within committed windows. P1s are business-critical events where every minute carries direct cost. Reclassifying slow incidents as P2 launders the number. Read with mean time to recover - service view and root cause analysis completion rate.

## Formula

```
P1 Incidents Resolved within SLA / P1 Incidents
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** it_incident_major_problem_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2884 (batch 7)
