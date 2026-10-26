# dea:metric-program-milestone-slip

Candidate Performance Metric record for **Program Milestone Slip** (PMS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-program-milestone-slip`
- **Name:** Program Milestone Slip
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PMS

## 2. Definition

Program Milestone Slip (PMS) addresses conformance to standards, plans, or obligations and is a fixture of defense & aerospace reporting. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Days of Schedule Slip at Milestone; the result is stated in days. It should be driven down, since lower readings signal healthier performance. In Defense & aerospace, it is a recognized element of the standard performance toolkit.

## 3. Context

Program milestone slip measures schedule growth against baselines at decision points, and it is the defense acquisition metric that explains why major weapons programs have historically averaged major schedule growth (GAO's annual weapon systems assessments document repeated double-digit delays). The structural causes are well understood: concurrency (producing while still developing), requirements creep, technology immaturity at milestones, and optimistic baselines used to win program approval. Slip is the compound-interest metric - delays extend fixed-cost burn and production gap, often doubling program cost before a single additional unit is delivered. Read with slip by milestone type (which phases overrun most, historically development test), requirements-change history, Earned Value schedule indices, and the critical path's external dependencies.

## Formula

```
Days of Schedule Slip at Milestone
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** defense_aerospace
- **Sector:** defense_aerospace

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 969 (batch 3)
