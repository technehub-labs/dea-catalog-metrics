# dea:metric-workforce-productivity-index

Candidate Performance Metric record for **Workforce Productivity Index** (WPI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-workforce-productivity-index`
- **Name:** Workforce Productivity Index
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** WPI

## 2. Definition

Workforce Productivity Index (WPI) captures how efficiently resources are converted into outputs for organizations tracking workforce planning & analytics. It is computed as Output Value per Labor Hour, Indexed to Baseline, expressed in index (0-100 or normalized). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

A composite of output measures per labor input, normalized to compare across units and periods. It is the neutral referee between automation claims, headcount reduction, and growth without hiring. Index construction is where honesty is won or lost: output definitions, quality adjustment, and mix effects all shift the number without any real change. Read with cost per unit trends and overtime usage for under-staffing distortions.

## Formula

```
Output Value per Labor Hour, Indexed to Baseline
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** organization
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1459 (batch 5)
