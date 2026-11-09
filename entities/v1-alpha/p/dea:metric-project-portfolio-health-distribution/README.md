# dea:metric-project-portfolio-health-distribution

Candidate Performance Metric record for **Project Portfolio Health Distribution** (PPHD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-project-portfolio-health-distribution`
- **Name:** Project Portfolio Health Distribution
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PPHD

## 2. Definition

A Project Management (Deep Dive) indicator, Project Portfolio Health Distribution (PPHD) quantifies exposure to adverse outcomes. Its calculation is Green Projects / Total Projects, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the proportion of projects at each health status (green, amber, red). Chronically green portfolios reveal reporting culture problems; real portfolios have ambers. Distribution skewed green before annual planning rounds invites skepticism. Read with risk exposure trend index and governance review compliance.

## Formula

```
PPHD = Green Projects / Total Projects
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
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** project_management_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2944 (batch 7)
