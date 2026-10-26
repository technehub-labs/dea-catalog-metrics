# dea:metric-schedule-performance-index

Candidate Performance Metric record for **Schedule Performance Index** (SPI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-schedule-performance-index`
- **Name:** Schedule Performance Index
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SPI

## 2. Definition

A Project Management indicator, Schedule Performance Index (SPI) quantifies conformance to standards, plans, or obligations. Its calculation is Earned Value / Planned Value, measured in ratio (x:1 or x). It is applied across virtually every sector. Its value drives prioritization and resource reallocation among competing initiatives. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

SPI, from Earned Value Management (a DoD/NASA tradition), is earned value divided by planned value - how much of the schedule scope you have actually accomplished versus plan. At 1.0 you are exactly on schedule; below 1.0 behind. Its strength is objectivity: progress is measured in budgeted work, not percent-complete opinions. Its caveat: SPI can approach 1.0 as a late project simply runs out of work to measure, so read it alongside the critical-path status, and remember SPI measures accomplishment, not the remaining work's realism.

## Formula

```
Earned Value / Planned Value
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** transformation
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** project_management

## Attribution

- **Source credit:** Earned Value Management (DoD/NASA tradition)

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 348 (batch 1)
