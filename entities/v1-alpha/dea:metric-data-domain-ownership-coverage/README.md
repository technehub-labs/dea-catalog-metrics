# dea:metric-data-domain-ownership-coverage

Candidate Performance Metric record for **Data Domain Ownership Coverage** (DDOC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-domain-ownership-coverage`
- **Name:** Data Domain Ownership Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DDOC

## 2. Definition

A Data Governance & Stewardship indicator, Data Domain Ownership Coverage (DDOC) quantifies governance. The formula is Data Domains with Named Accountable Owner / Domains - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of data domains with accountable, named owners. Unowned domains are where quality decays unchecked. Ownership without stewardship resourcing is title, not ownership. Read with data governance policy adoption rate and critical data element governance coverage.

## Formula

```
DDOC = Data Domains with Named Accountable Owner / Domains
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** governance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3596 (batch 8)
