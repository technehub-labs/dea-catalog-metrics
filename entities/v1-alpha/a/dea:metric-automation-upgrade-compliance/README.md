# dea:metric-automation-upgrade-compliance

Candidate Performance Metric record for **Automation Upgrade Compliance** (AUC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-automation-upgrade-compliance`
- **Name:** Automation Upgrade Compliance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** AUC

## 2. Definition

Within Industrial Automation & Robotics, Automation Upgrade Compliance (AUC) is used to gauge conformance to standards, plans, or obligations. It is a working-level control: thresholds trigger immediate operational response. It is defined as Cells Running Current Firmware and Safety Config / Cells; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. In Manufacturing, it is a recognized element of the standard performance toolkit.

## Formula

```
AUC = Cells Running Current Firmware and Safety Config / Cells
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** industrial_automation_robotics
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1343 (batch 5)
