# dea:metric-space-cost-per-workstation

Candidate Performance Metric record for **Space Cost per Workstation** (SCPW) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-space-cost-per-workstation`
- **Name:** Space Cost per Workstation
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SCPW

## 2. Definition

Within Facility Management & Workplace (Deep Dive), Space Cost per Workstation (SCPW) is used to gauge how efficiently resources are converted into outputs. The formula is Total Facility Cost / Workstations - reported in currency per unit. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures total occupancy cost allocated per workstation or seat. It is the unit economics of corporate real estate, and it is the metric that portfolio strategies (hub-and-spoke, hot-desking, flex) must improve to justify themselves. Allocation methodology hides as much as it reveals - shared space, vacant floors, and shadow costs need consistent treatment. Read with desk utilization rate (Deep Dive) and total occupancy cost trend against headcount.

## Formula

```
Total Facility Cost / Workstations
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** facility_management_workplace_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2246 (batch 6)
