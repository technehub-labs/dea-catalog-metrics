# dea:metric-esg-data-completeness-rate

Candidate Performance Metric record for **ESG Data Completeness Rate** (ESGDC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-esg-data-completeness-rate`
- **Name:** ESG Data Completeness Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ESGDC

## 2. Definition

Within Environmental, Social & Governance Reporting, ESG Data Completeness Rate (ESGDC) is used to gauge conformance to standards, plans, or obligations. Its calculation is Reported Data Points / Required Data Points, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of required ESG data points populated with quality evidence. Completeness is the gating constraint of ESG reporting: frameworks are expanding into regulated disclosure with assurance attached, and gaps now carry legal rather than reputational consequence. Weight completeness by materiality and evidence quality, since a filled field with an estimate is not the same as one with measured data. Read with assurance readiness score (ESG) and restatement rate (ESG Disclosures).

## Formula

```
Reported Data Points / Required Data Points
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** environmental_social_governance_reporting

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2192 (batch 6)
