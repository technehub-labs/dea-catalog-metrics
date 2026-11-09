# dea:metric-red-team-containment-time

Candidate Performance Metric record for **Red Team Containment Time** (RTCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-red-team-containment-time`
- **Name:** Red Team Containment Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RTCT

## 2. Definition

Within Threat Intelligence & Red Team, Red Team Containment Time (RTCT) is used to gauge exposure to adverse outcomes. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Time for Defenders to Contain Simulated Intrusion - reported in hours. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how long blue teams take to contain simulated attacker activity once detected. Containment speed determines how much damage a real intruder could do. Containment declared without verifying attacker persistence (additional footholds) is premature. Read with red team detection rate and mean time to contain - security.

## Formula

```
RTCT = Time for Defenders to Contain Simulated Intrusion
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** threat_intelligence_red_team

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3285 (batch 7)
