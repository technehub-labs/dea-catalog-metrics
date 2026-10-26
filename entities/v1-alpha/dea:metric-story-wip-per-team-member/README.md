# dea:metric-story-wip-per-team-member

Candidate Performance Metric record for **Story WIP per Team Member** (SWTM-AG) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-story-wip-per-team-member`
- **Name:** Story WIP per Team Member
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SWTM-AG

## 2. Definition

Story WIP per Team Member (SWTM-AG) captures how efficiently resources are converted into outputs for organizations tracking agile delivery & team effectiveness. It provides the day-to-day signal that a process is running as designed. Its calculation is In-Progress Stories / Team Members, measured in count (items per period). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
In-Progress Stories / Team Members
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** organization
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** agile_delivery_team_effectiveness

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2982 (batch 7)
