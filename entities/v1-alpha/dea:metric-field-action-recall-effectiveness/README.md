# dea:metric-field-action-recall-effectiveness

Candidate Performance Metric record for **Field Action Recall Effectiveness** (FARE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-field-action-recall-effectiveness`
- **Name:** Field Action Recall Effectiveness
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FARE

## 2. Definition

Field Action Recall Effectiveness (FARE) measures exposure to adverse outcomes in the Medical Devices domain. The formula is Devices Corrected or Removed / Devices Subject to Field Action - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Medical devices sector.

## 3. Context

Field action recall effectiveness measures the completion rate of corrective actions deployed to devices already in the field, and it is where a recall stops being a press release and becomes a real patient-safety outcome. The challenge is structural: devices are embedded in hospitals, home settings, and third-party distributors, each with different reach-back mechanisms, so effectiveness varies widely by channel. A manufacturer can issue a field action and still have thousands of unrepaired units in circulation months later. Read alongside completion rate by segment and time-to-completion curves, since the units remaining at the tail of the curve are the riskiest to leave unreached.

## Formula

```
Devices Corrected or Removed / Devices Subject to Field Action
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
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** medical_devices
- **Sector:** medical_devices

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 758 (batch 2)
