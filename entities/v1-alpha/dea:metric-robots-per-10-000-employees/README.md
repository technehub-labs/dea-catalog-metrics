# dea:metric-robots-per-10-000-employees

Candidate Performance Metric record for **Robots per 10,000 Employees** (RD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-robots-per-10-000-employees`
- **Name:** Robots per 10,000 Employees
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RD

## 2. Definition

Robots per 10,000 Employees (RD) captures capability maturity or development for organizations tracking industrial automation & robotics. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Industrial Robots in Operation / Employees x 10,000, expressed in events per thousand or million (scaled). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Manufacturing.

## 3. Context

Measures robot density relative to workforce, the standard cross-country benchmark of industrial automation intensity. It signals capital-deepening and productivity potential, but density alone says nothing about whether the robots are well-utilized or what happened to the people. Comparisons mislead when robot classes (industrial arms versus cobots versus AMRs) are mixed. Read with capacity utilization and value added per worker, not headcount alone.

## Formula

```
RD = Industrial Robots in Operation / Employees x 10,000
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** industrial_automation_robotics
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1336 (batch 5)
