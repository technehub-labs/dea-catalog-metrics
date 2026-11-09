# dea:metric-mean-flight-hours-between-failures

Candidate Performance Metric record for **Mean Flight Hours between Failures** (MFHBF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mean-flight-hours-between-failures`
- **Name:** Mean Flight Hours between Failures
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MFHBF

## 2. Definition

Within Defense & Aerospace, Mean Flight Hours between Failures (MFHBF) is used to gauge exposure to adverse outcomes. The formula is Total Flight Hours / In-Flight Failures - reported in hours. It is a standard measure in the Defense & aerospace sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Mean flight hours between failures measures the reliability of aircraft systems in operational terms, and it is the metric that connects aircraft maintenance economics to fleet availability - each failure grounds aircraft and consumes wrench-turn hours, so reliability per flight hour drives both MC rate and maintenance cost. The metric matters strategically for fleet management: mission-design-series aging shows up here first, since hours accumulate unevenly across fleets and drive both scheduled and unscheduled maintenance. The decomposition principle applies with force: subsystem failure distribution (avionics, hydraulics, engines) identifies the specific reliability driver, and unscheduled versus scheduled maintenance ratio reveals whether the fleet is flying on a sustainable maintenance program. Read with subsystem Pareto analysis, failure rate by tail age cohort, and shop-visit intervals as the depot-level consequence.

## Formula

```
MFHBF = Total Flight Hours / In-Flight Failures
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** defense_aerospace
- **Sector:** defense_aerospace

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 968 (batch 3)
