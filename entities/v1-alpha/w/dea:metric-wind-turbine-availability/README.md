# dea:metric-wind-turbine-availability

Candidate Performance Metric record for **Wind Turbine Availability** (WTA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-wind-turbine-availability`
- **Name:** Wind Turbine Availability
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** WTA

## 2. Definition

Wind Turbine Availability (WTA) measures the utilization or availability of capacity in the Energy Transition & Renewables domain. It is defined as Turbine Available Hours / Total Hours; the result is stated in percent (%). In Renewable energy, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Wind turbine availability measures the share of time turbines are capable of operating, and it is the operational backbone metric of wind-project economics - the capital is sunk and the resource (wind) is free, so every hour of unavailability is revenue lost that can never be recovered. Contractual availability (warranty and O&M agreements typically specify 97 percent thresholds) and production-based availability differ: a turbine can be technically available and still produce nothing when wind is absent, so production-weighted measurement (lost-production accounting) is the honest economic version. Failure-mode distribution is the improvement map: gearboxes, generators, and blades carry high-cost failures, and the preventive-maintenance-versus-condition-monitoring trade-off is where operators optimize. Read with capacity factor as the economic composite, mean time to repair (access logistics for offshore - vessel availability dominates offshore repair time), and warranty-claim performance.

## Formula

```
WTA = Turbine Available Hours / Total Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** energy_transition_renewables
- **Sector:** renewable_energy

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1102 (batch 4)
