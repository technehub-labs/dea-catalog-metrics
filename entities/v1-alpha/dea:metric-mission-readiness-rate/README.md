# dea:metric-mission-readiness-rate

Candidate Performance Metric record for **Mission Readiness Rate** (MRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mission-readiness-rate`
- **Name:** Mission Readiness Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MRR

## 2. Definition

Mission Readiness Rate (MRR) addresses the utilization or availability of capacity and is a fixture of aerospace & defense program management reporting. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Assets Ready for Mission / Assigned Assets, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Aerospace & Defense.

## 3. Context

Measures the share of systems, units, or platforms ready for their assigned mission at required capability levels. It is the output metric of the entire sustainment system: supply, maintenance, and manpower all converge here. Readiness defined as available-but-degraded hides capability gaps, so readiness levels must be capability-based. Read with aircraft mission capability rate and mission success rate context.

## Formula

```
MRR = Assets Ready for Mission / Assigned Assets
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** aerospace_defense_program_management
- **Sector:** aerospace_defense

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1791 (batch 6)
