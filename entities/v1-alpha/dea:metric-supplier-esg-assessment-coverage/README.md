# dea:metric-supplier-esg-assessment-coverage

Candidate Performance Metric record for **Supplier ESG Assessment Coverage** (SESG) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-supplier-esg-assessment-coverage`
- **Name:** Supplier ESG Assessment Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SESG

## 2. Definition

Within Sustainability & ESG, Supplier ESG Assessment Coverage (SESG) is used to gauge conformance to standards, plans, or obligations. The formula is Key Suppliers ESG-Assessed / Key Suppliers - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

The share of in-scope suppliers assessed against environmental, social, and governance criteria - the coverage metric that extends ESG accountability upstream, since most organizations carry the large majority of their footprint in their supply base rather than their own operations. Its strategic weight is regulatory cascade: disclosure regimes from the EU supply-chain directives onward make large firms answer for their suppliers' conduct, and assessment coverage is the primary due-diligence evidence when an incident surfaces. The honest construction is tiered and weighted: covering the top suppliers by spend and risk-depth matters far more than counting long-tail questionnaires, and coverage weighted by emissions or spend share tells a different story than coverage by count. Read with the action rate: assessment without follow-up is observation, and the share of flagged suppliers with remediation plans is where coverage becomes management.

## Formula

```
Key Suppliers ESG-Assessed / Key Suppliers
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** sustainability_esg

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 423 (batch 1)
