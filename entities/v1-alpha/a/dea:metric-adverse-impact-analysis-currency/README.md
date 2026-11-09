# dea:metric-adverse-impact-analysis-currency

Candidate Performance Metric record for **Adverse Impact Analysis Currency** (AIAC-E) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-adverse-impact-analysis-currency`
- **Name:** Adverse Impact Analysis Currency
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** AIAC-E

## 2. Definition

Adverse Impact Analysis Currency (AIAC-E) captures conformance to standards, plans, or obligations for organizations tracking ai ethics, fairness & responsible ai. Its calculation is Analyses Completed within Required Cycle / Due, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures whether adverse impact analyses are current for selection systems in active use. Adverse impact analysis is the evidentiary standard in employment discrimination exposure, and currency matters because impact shifts with applicant pools, model updates, and role changes. Stale analyses defend yesterday's decisions, which is precisely what litigation examines. Read with disparate impact ratio (Deep Dive) trends and analysis-refresh triggers on process changes.

## Formula

```
AIAC-E = Analyses Completed within Required Cycle / Due
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** ai_ethics_fairness_responsible_ai

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2571 (batch 7)
