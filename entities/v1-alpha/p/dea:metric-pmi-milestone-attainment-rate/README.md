# dea:metric-pmi-milestone-attainment-rate

Candidate Performance Metric record for **PMI Milestone Attainment Rate** (PMMA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-pmi-milestone-attainment-rate`
- **Name:** PMI Milestone Attainment Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PMMA

## 2. Definition

PMI Milestone Attainment Rate (PMMA) measures conformance to standards, plans, or obligations in the Mergers & Acquisitions domain. Its calculation is Integration Milestones on Schedule / Milestones, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures delivery of integration plan milestones - systems cutover, org design, process harmonization, brand transition - on schedule. It is the management heartbeat of integration: slippage compounds, and integration debt is harder to clear the longer it lingers. Watch for milestone redefinition as the standard cover for slip, and for critical-path items traded for cosmetic green. Read with integration cost overrun rate and synergy realization timing.

## Formula

```
PMMA = Integration Milestones on Schedule / Milestones
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** mergers_acquisitions

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1701 (batch 6)
