# dea:metric-single-points-of-dependency-count

Candidate Performance Metric record for **Single Points of Dependency Count** (SPOD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-single-points-of-dependency-count`
- **Name:** Single Points of Dependency Count
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SPOD

## 2. Definition

Within Business Continuity & Disaster Recovery, Single Points of Dependency Count (SPOD) is used to gauge exposure to adverse outcomes. It is computed as Critical Dependencies without Redundancy / Critical Dependencies, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the count of critical functions resting on single systems, people, suppliers, or sites. Each single point is a concentrated fragility waiting for its trigger. Counts limited to technical single points miss people and supplier dependencies. Read with single points of failure analysis and strategic dependency concentration (Alliances).

## Formula

```
SPOD = Critical Dependencies without Redundancy / Critical Dependencies
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** business_continuity_disaster_recovery

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3524 (batch 8)
