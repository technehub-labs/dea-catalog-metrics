# dea:metric-foreign-object-damage-rate

Candidate Performance Metric record for **Foreign Object Damage Rate** (FODR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-foreign-object-damage-rate`
- **Name:** Foreign Object Damage Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FODR

## 2. Definition

Within Defense & Aerospace, Foreign Object Damage Rate (FODR) is used to gauge the quality of outputs and outcomes. It is defined as Foreign Object Damage Events / Flight Hours x 1,000; the result is stated in events per thousand or million (scaled). In Defense & aerospace, it is a recognized element of the standard performance toolkit. It is a working-level control: thresholds trigger immediate operational response. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Foreign Object Damage Events / Flight Hours x 1,000
```

## Unit

- **Unit reference:** `dea:unit-events`
- **Unit:** events
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** defense_aerospace
- **Sector:** defense_aerospace

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 975 (batch 3)
