# dea:metric-algorithmic-bias-audit-coverage

Candidate Performance Metric record for **Algorithmic Bias Audit Coverage** (ABAC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-algorithmic-bias-audit-coverage`
- **Name:** Algorithmic Bias Audit Coverage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ABAC

## 2. Definition

A AI Ethics, Fairness & Responsible AI indicator, Algorithmic Bias Audit Coverage (ABAC) quantifies exposure to adverse outcomes. Its calculation is High-Risk Models Audited for Bias / High-Risk Models, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of consequential decision systems audited for bias. Bias audits are the point-in-time assessment layer beneath continuous monitoring, and coverage gaps concentrate in the lower-visibility decisions (screening, ranking, prioritization) that still shape opportunities. Audit independence and methodology determine whether coverage is assurance or paperwork. Read with bias remediation closure rate (Deep Dive) and audit-finding severity distribution.

## Formula

```
High-Risk Models Audited for Bias / High-Risk Models
```

## Unit

- **Unit reference:** `dea:unit-percent`
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
- **Domain:** ai_ethics_fairness_responsible_ai

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2565 (batch 7)
