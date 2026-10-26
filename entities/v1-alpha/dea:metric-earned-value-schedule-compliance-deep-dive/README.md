# dea:metric-earned-value-schedule-compliance-deep-dive

Candidate Performance Metric record for **Earned Value Schedule Compliance (Deep Dive)** (EVSC-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-earned-value-schedule-compliance-deep-dive`
- **Name:** Earned Value Schedule Compliance (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** EVSC-D

## 2. Definition

Earned Value Schedule Compliance (Deep Dive) (EVSC-D) measures conformance to standards, plans, or obligations in the Aerospace & Defense Program Management domain. Its calculation is Milestones with SPI >= 0.95 / Milestones, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Aerospace & Defense practice.

## 3. Context

Measures schedule performance through earned value management, comparing work performed against the baseline. In long-duration defense and aerospace programs, EVM is the contractual and diagnostic lingua franca, and SV trends reveal problems that milestone reporting smooths over. EVM integrity depends on BCWS quality: biased baselines produce confident nonsense. Read with schedule performance index (Programs) and milestone achievement confidence.

## Formula

```
Milestones with SPI >= 0.95 / Milestones
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** compliance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1778 (batch 6)
