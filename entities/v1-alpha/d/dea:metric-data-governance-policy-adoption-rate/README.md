# dea:metric-data-governance-policy-adoption-rate

Candidate Performance Metric record for **Data Governance Policy Adoption Rate** (DGPRA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-governance-policy-adoption-rate`
- **Name:** Data Governance Policy Adoption Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DGPRA

## 2. Definition

Within Data Governance & Stewardship, Data Governance Policy Adoption Rate (DGPRA) is used to gauge conformance to standards, plans, or obligations. It is computed as Business Units with Adopted Charter / Business Units, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how widely the governed data policies are actually followed across units. Policy without adoption is documentation. Adoption measured by training completion rather than behavior is illusory. Read with data governance maturity score and data classification coverage.

## Formula

```
DGPRA = Business Units with Adopted Charter / Business Units
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** data_governance_stewardship

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3595 (batch 8)
