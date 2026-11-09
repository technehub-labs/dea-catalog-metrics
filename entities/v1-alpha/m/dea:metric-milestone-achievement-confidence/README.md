# dea:metric-milestone-achievement-confidence

Candidate Performance Metric record for **Milestone Achievement Confidence** (MAC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-milestone-achievement-confidence`
- **Name:** Milestone Achievement Confidence
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MAC

## 2. Definition

Milestone Achievement Confidence (MAC) measures exposure to adverse outcomes in the Aerospace & Defense Program Management domain. The formula is Program Milestones at Green Confidence / Milestones - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Aerospace & Defense sector.

## 3. Context

Measures the confidence-weighted probability that program milestones will be met, typically from integrated program risk assessments. It converts schedule risk from a static plan into a live forecast, and confidence deterioration is the early warning before slip becomes official. Beware optimism inertia: confidence scores anchored to committed dates drift downward too slowly. Read with schedule performance index (Programs) and independent schedule assessments.

## Formula

```
MAC = Program Milestones at Green Confidence / Milestones
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** aerospace_defense_program_management
- **Sector:** aerospace_defense

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1777 (batch 6)
