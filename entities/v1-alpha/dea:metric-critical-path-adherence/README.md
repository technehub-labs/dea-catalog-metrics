# dea:metric-critical-path-adherence

Candidate Performance Metric record for **Critical Path Adherence** (CPA-PM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-critical-path-adherence`
- **Name:** Critical Path Adherence
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CPA-PM

## 2. Definition

Critical Path Adherence (CPA-PM) captures exposure to adverse outcomes for organizations tracking project management (deep dive). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Critical Path Activities on Schedule / Critical Path Activities - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how well the project protects schedule on its longest dependent task chain. Only critical-path delays move the end date; everything else is noise. Focusing effort on visible tasks rather than critical ones wastes leverage. Read with milestone hit rate and dependency closure timeliness.

## Formula

```
Critical Path Activities on Schedule / Critical Path Activities
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** project_management_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2934 (batch 7)
