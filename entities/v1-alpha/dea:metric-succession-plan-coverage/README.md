# dea:metric-succession-plan-coverage

Candidate Performance Metric record for **Succession Plan Coverage** (SPC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-succession-plan-coverage`
- **Name:** Succession Plan Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SPC

## 2. Definition

Succession Plan Coverage (SPC) measures exposure to adverse outcomes in the Human Resources domain. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Critical Roles with Ready Successors / Critical Roles; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The share of critical roles with a named, development-tracked successor - the continuity metric that boards ask for after every abrupt CEO departure makes the news. Its strategic weight is asymmetry of risk: unplanned vacancies in critical roles disrupt strategy execution for quarters, and coverage below full for genuinely critical roles is an unmanaged exposure that compensation committees now treat as part of governance quality. The honest construction has teeth - a real plan means a named successor who has been told, with development actions in motion, not a name in a spreadsheet - and depth matters as much as breadth: coverage with one ready-now successor per role is stronger than two successors who are all years away. Read with the internal promotion rate, which shows whether the pipeline actually flows.

## Formula

```
SPC = Critical Roles with Ready Successors / Critical Roles
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** human_resources

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 142 (batch 1)
