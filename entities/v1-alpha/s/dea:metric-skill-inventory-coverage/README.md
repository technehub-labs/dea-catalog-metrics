# dea:metric-skill-inventory-coverage

Candidate Performance Metric record for **Skill Inventory Coverage** (SIC-W) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-skill-inventory-coverage`
- **Name:** Skill Inventory Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SIC-W

## 2. Definition

Skill Inventory Coverage (SIC-W) measures capability maturity or development in the Workforce Planning & Analytics domain. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Employees with Current Skills Profile / Employees - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of the workforce with verified, current skill profiles in the skills taxonomy. It is the foundation for internal mobility, staffing analytics, and AI-era reskilling programs; without it, workforce planning is job-title guesswork. Beware self-reported skills without assessment, and taxonomies so granular they cannot be maintained. Read with skill gap closure rates and internal fill rates for openings.

## Formula

```
SIC-W = Employees with Current Skills Profile / Employees
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** workforce_planning_analytics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1452 (batch 5)
