# dea:metric-safety-incidents-in-automated-cells

Candidate Performance Metric record for **Safety Incidents in Automated Cells** (SIAC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-safety-incidents-in-automated-cells`
- **Name:** Safety Incidents in Automated Cells
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SIAC

## 2. Definition

Safety Incidents in Automated Cells (SIAC) captures exposure to adverse outcomes for organizations tracking industrial automation & robotics. The formula is Recordable Incidents in Automated Areas / Period - reported in count (items per period). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. It is a standard measure in the Manufacturing sector.

## 3. Context

Tracks recordable injuries and near-misses occurring in or around automated production cells. It matters because automation shifts rather than eliminates risk - lockout failures, unexpected restarts, and human-robot interaction points become the new injury frontier. Watch for underreporting as cells run to maintenance-avoidance targets, and normalize by exposure hours, not cell count. Read with robot utilization and maintenance interventions, since interrupted cells breed improvisation.

## Formula

```
Recordable Incidents in Automated Areas / Period
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** industrial_automation_robotics
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1341 (batch 5)
