# dea:metric-compliance-risk-assessment-coverage

Candidate Performance Metric record for **Compliance Risk Assessment Coverage** (CRAC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-compliance-risk-assessment-coverage`
- **Name:** Compliance Risk Assessment Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CRAC

## 2. Definition

Compliance Risk Assessment Coverage (CRAC) addresses exposure to adverse outcomes and is a fixture of regulatory affairs & compliance operations reporting. It is computed as Business Units Assessed / Units in Scope, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of business lines, products, and jurisdictions covered by current compliance risk assessments. Coverage gaps are where compliance failures incubate, particularly in fast-growing or newly launched offerings. Freshness counts as much as breadth: assessments predating material business change are negative coverage. Read with regulatory change management throughput and audit findings in unassessed areas.

## Formula

```
Business Units Assessed / Units in Scope
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** regulatory_affairs_compliance_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1597 (batch 6)
