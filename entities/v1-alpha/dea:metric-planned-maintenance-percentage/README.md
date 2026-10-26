# dea:metric-planned-maintenance-percentage

Candidate Performance Metric record for **Planned Maintenance Percentage** (PMP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-planned-maintenance-percentage`
- **Name:** Planned Maintenance Percentage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PMP

## 2. Definition

A Maintenance & Reliability indicator, Planned Maintenance Percentage (PMP) quantifies exposure to adverse outcomes. The formula is Planned Maintenance Hours / Total Maintenance Hours - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Manufacturing sector.

## 3. Context

The share of maintenance hours that are planned rather than reactive - the maturity dial of the maintenance function, because planned work is executed at a fraction of the cost of breakdown work and does not interrupt production. Levels below 50 percent mean the maintenance organization is predominantly a fire brigade, and every other reliability metric - availability, breakdown frequency, maintenance cost per unit - is downstream of this one. The strategic logic is preventive economics: each dollar of planning prevents multiple dollars of emergency work, overtime, and downtime, which is why raising this percentage is almost always the first move of a reliability program. The transition matters: planned-percentage improvements that come from over-planning (performing unneeded scheduled work) waste the gain, so it is read together with scheduled-work compliance and failure rates.

## Formula

```
Planned Maintenance Hours / Total Maintenance Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** maintenance_reliability
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 265 (batch 1)
