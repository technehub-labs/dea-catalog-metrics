# dea:metric-escaped-defect-rate-per-sprint

Candidate Performance Metric record for **Escaped Defect Rate per Sprint** (EDR-AG) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-escaped-defect-rate-per-sprint`
- **Name:** Escaped Defect Rate per Sprint
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** EDR-AG

## 2. Definition

Escaped Defect Rate per Sprint (EDR-AG) measures the quality of outputs and outcomes in the Agile Delivery & Team Effectiveness domain. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Production Defects Attributed to Sprint / Sprint Deliverables - reported in events per thousand or million (scaled). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures defects found post-sprint per unit of delivery. It is the sprint-level quality leak metric that predicts production pain. Defects traced to poorly understood acceptance criteria, not just coding, complicate attribution. Read with defect escape rate and change failure rate.

## Formula

```
Production Defects Attributed to Sprint / Sprint Deliverables
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** organization
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** agile_delivery_team_effectiveness

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2991 (batch 7)
