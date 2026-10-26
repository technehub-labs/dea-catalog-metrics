# dea:metric-project-success-rate

Candidate Performance Metric record for **Project Success Rate** (PSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-project-success-rate`
- **Name:** Project Success Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PSR

## 2. Definition

A Project Management indicator, Project Success Rate (PSR) quantifies how effectively a process or entity achieves its intended outcome. It is defined as Projects Meeting Scope, Schedule, Budget / Total Projects; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The share of projects delivered meeting their baseline for scope, schedule, and cost - the headline accountability metric of the project organization, given teeth by decades of research (the Standish tradition and successors) showing how commonly projects fail against their original commitments. Its strategic content is definitional honesty: a rate computed against silently re-baselined projects is a comfortable fiction, so mature organizations distinguish success against original baseline from success against latest baseline and report both. The rate is a portfolio symptom rather than a team score - chronic misses usually indicate estimation culture, approval discipline, or scope governance problems rather than execution weakness, which is why interventions that target project managers rarely move it. Read with the size distribution: small projects succeed far more often than large ones, so mix shifts can move the rate without any capability change.

## Formula

```
PSR = Projects Meeting Scope, Schedule, Budget / Total Projects
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** transformation
- **Purpose classification:** effectiveness
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** project_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 352 (batch 1)
