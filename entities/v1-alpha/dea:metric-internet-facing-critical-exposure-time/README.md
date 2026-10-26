# dea:metric-internet-facing-critical-exposure-time

Candidate Performance Metric record for **Internet-Facing Critical Exposure Time** (IFCET) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-internet-facing-critical-exposure-time`
- **Name:** Internet-Facing Critical Exposure Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** IFCET

## 2. Definition

Internet-Facing Critical Exposure Time (IFCET) measures exposure to adverse outcomes in the Vulnerability & Exposure Management domain. The formula is Hours Critical Vulnerability Remains Internet-Exposed - reported in hours. It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures how long critical vulnerabilities remain unremediated on internet-connected assets. Exposure time, not count, is what attackers exploit; a single critical facing the internet for weeks is an incident waiting to happen. Scheduling fixes in monthly windows guarantees some exposure. Read with zero-day response time and open critical vulnerability count.

## Formula

```
Hours Critical Vulnerability Remains Internet-Exposed
```

## Unit

- **Unit reference:** `dea:unit-hours`
- **Unit:** hours
- **Unit label (as published):** hours

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** vulnerability_exposure_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2808 (batch 7)
