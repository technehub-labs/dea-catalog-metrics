# dea:metric-purple-team-exercise-improvement-rate

Candidate Performance Metric record for **Purple Team Exercise Improvement Rate** (PTEIR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-purple-team-exercise-improvement-rate`
- **Name:** Purple Team Exercise Improvement Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PTEIR

## 2. Definition

Purple Team Exercise Improvement Rate (PTEIR) addresses capability maturity or development and is a fixture of secops & security operations center reporting. The formula is Detections Improved after Exercises / Gaps Identified - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how detection coverage improves following purple team validation exercises. Purple teaming converts red-team findings into durable blue-team capability. Improvement requires tracking specific rule fixes, not declaring victory after the session. Read with detection rule health and tabletop exercise completion rate.

## Formula

```
PTEIR = Detections Improved after Exercises / Gaps Identified
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2792 (batch 7)
