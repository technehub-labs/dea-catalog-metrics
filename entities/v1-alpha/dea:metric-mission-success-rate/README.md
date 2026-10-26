# dea:metric-mission-success-rate

Candidate Performance Metric record for **Mission Success Rate** (MSR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mission-success-rate`
- **Name:** Mission Success Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MSR-D

## 2. Definition

Mission Success Rate (MSR-D) measures how effectively a process or entity achieves its intended outcome in the Defense & Aerospace domain. Its calculation is Missions Achieving Objectives / Missions Executed, measured in percent (%). It originates from and is most used in Defense & aerospace practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Mission success rate measures the share of operations achieving objectives, and it is the defining effectiveness metric of defense organizations - the metric that justifies the entire apparatus, with the moral weight of lives and national security riding on it. Its measurement is uniquely hard because missions vary enormously in complexity and conditions, so a raw rate conflates capability with mission difficulty mix. The mission-type decomposition is the honest approach: success rates by operation class (air superiority, ISR, logistics, humanitarian) track real capability better than blended figures. The gaming risk is definitional - what counts as success in a counterinsurgency or stability operation resists binary measurement entirely. Read with success rate by operation type, partial-success attribution, Blue Force Tracker and post-mission reporting data quality, and readiness-to-mission linkage.

## Formula

```
Missions Achieving Objectives / Missions Executed
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** defense_aerospace
- **Sector:** defense_aerospace

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 966 (batch 3)
