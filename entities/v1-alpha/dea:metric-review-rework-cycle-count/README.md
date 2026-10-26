# dea:metric-review-rework-cycle-count

Candidate Performance Metric record for **Review Rework Cycle Count** (RRC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-review-rework-cycle-count`
- **Name:** Review Rework Cycle Count
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RRC

## 2. Definition

Review Rework Cycle Count (RRC) captures how efficiently resources are converted into outputs for organizations tracking code review & peer quality. It provides the day-to-day signal that a process is running as designed. Its calculation is Average Revision Cycles before Approval, measured in times per period. It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Software practice.

## Formula

```
Average Revision Cycles before Approval
```

## Unit

- **Unit reference:** `dea:unit-times`
- **Unit:** times
- **Unit label (as published):** times per period

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** code_review_peer_quality
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3198 (batch 7)
