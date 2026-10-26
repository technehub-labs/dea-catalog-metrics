# dea:metric-earned-value-schedule-compliance

Candidate Performance Metric record for **Earned Value Schedule Compliance** (EVSC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-earned-value-schedule-compliance`
- **Name:** Earned Value Schedule Compliance
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** EVSC

## 2. Definition

A Defense & Aerospace indicator, Earned Value Schedule Compliance (EVSC) quantifies conformance to standards, plans, or obligations. It is defined as Earned Value / Planned Value at Milestone; the result is stated in ratio (x:1 or x). In Defense & aerospace, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Earned Value schedule compliance measures schedule performance using the EV framework - schedule performance index (earned value divided by planned value) - and it is the metric that defense acquisition (and project management broadly, per the DoD's EVMS doctrine) relies on for objective progress measurement. Its power is the falsifiability it adds to percent-complete claims: physical percent complete measured in objective terms is harder to game than opinion-based status. Its weakness is the quality of the underlying measurement: earned value can be technically compliant while measuring the wrong things (easy tasks done first), and SPI approaching 1.0 on a late baseline (after rebaselining) erases history. Read with SPI trend rather than point-in-time, critical-path versus SPI divergence, cost performance index for the companion view, and baseline-change history for the honesty check.

## Formula

```
Earned Value / Planned Value at Milestone
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 970 (batch 3)
