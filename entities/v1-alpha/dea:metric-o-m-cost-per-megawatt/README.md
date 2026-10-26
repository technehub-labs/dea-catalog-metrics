# dea:metric-o-m-cost-per-megawatt

Candidate Performance Metric record for **O&M Cost per Megawatt** (OMCMW) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-o-m-cost-per-megawatt`
- **Name:** O&M Cost per Megawatt
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** OMCMW

## 2. Definition

O&M Cost per Megawatt (OMCMW) addresses how efficiently resources are converted into outputs and is a fixture of energy transition & renewables reporting. It is defined as Operations and Maintenance Cost / Installed Capacity; the result is stated in currency per unit. In Renewable energy, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

O&M cost per megawatt measures the annual operating and maintenance expense normalized by installed capacity, and it is the operating-cost efficiency metric of renewable portfolios - LCOE's dominant post-construction component, since fuel is free and the cost story is construction (fixed) plus O&M (ongoing). The metric's structure divides into planned maintenance (scheduled inspection and servicing) and unplanned (corrective repair), with unplanned costs carrying the leverage: reactive maintenance costs more than preventive, and condition-based maintenance (vibration monitoring, drone blade inspection, SCADA analytics) is the modern optimization frontier. Portfolio scale matters: O&M cost per MW declines with fleet scale (shared technician coverage, spare-parts inventory amortization), which is a genuine driver of consolidation in renewables. Read with availability and capacity factor (cost savings must not come through them), planned-versus-reactive maintenance ratio, and warranty-versus-self-perform cost differential.

## Formula

```
Operations and Maintenance Cost / Installed Capacity
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** energy_transition_renewables
- **Sector:** renewable_energy

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1107 (batch 4)
