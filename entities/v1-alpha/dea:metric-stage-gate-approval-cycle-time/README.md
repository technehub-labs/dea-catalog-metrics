# dea:metric-stage-gate-approval-cycle-time

Candidate Performance Metric record for **Stage Gate Approval Cycle Time** (SGACT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-stage-gate-approval-cycle-time`
- **Name:** Stage Gate Approval Cycle Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SGACT

## 2. Definition

Stage Gate Approval Cycle Time (SGACT) addresses how efficiently resources are converted into outputs and is a fixture of project management (deep dive) reporting. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Days to Complete Stage Gate Review, measured in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Days to Complete Stage Gate Review
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** project_management_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2954 (batch 7)
