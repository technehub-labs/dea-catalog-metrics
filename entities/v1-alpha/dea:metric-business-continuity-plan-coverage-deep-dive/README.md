# dea:metric-business-continuity-plan-coverage-deep-dive

Candidate Performance Metric record for **Business Continuity Plan Coverage (Deep Dive)** (BCPC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-business-continuity-plan-coverage-deep-dive`
- **Name:** Business Continuity Plan Coverage (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** BCPC

## 2. Definition

Within Business Continuity & Disaster Recovery, Business Continuity Plan Coverage (Deep Dive) (BCPC) is used to gauge exposure to adverse outcomes. It is defined as Critical Processes with Current BCP / Critical Processes; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of critical business functions with current, tested continuity plans. Coverage is the precondition: uncovered critical functions are unprepared by definition. Plans covering functions but not their dependencies (suppliers, systems) are incomplete. Read with business impact analysis currency and continuity plan activation success rate.

## Formula

```
Critical Processes with Current BCP / Critical Processes
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** business_continuity_disaster_recovery

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3515 (batch 8)
