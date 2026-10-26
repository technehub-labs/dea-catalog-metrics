# dea:metric-asset-integrity-completion-rate-chemicals

Candidate Performance Metric record for **Asset Integrity Completion Rate (Chemicals)** (AICR-C) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-asset-integrity-completion-rate-chemicals`
- **Name:** Asset Integrity Completion Rate (Chemicals)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** AICR-C

## 2. Definition

Within Chemicals & Specialty Materials, Asset Integrity Completion Rate (Chemicals) (AICR-C) is used to gauge exposure to adverse outcomes. Its calculation is Integrity Inspections Completed per Plan / Planned, measured in percent (%). It originates from and is most used in Chemicals practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures completion of mechanical integrity inspection, testing, and preventive maintenance schedules for pressure equipment and safety-critical systems. Deferred integrity work is how process safety incidents are scheduled in advance, so completion rate is the leading indicator regulators increasingly track. Prioritize by safety-critical classification rather than completion counts. Read with process safety event rate (Deep Dive) and corrosion-under-inspection findings.

## Formula

```
Integrity Inspections Completed per Plan / Planned
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** chemicals_specialty_materials
- **Sector:** chemicals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1817 (batch 6)
