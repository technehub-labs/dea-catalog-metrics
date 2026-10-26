# dea:metric-enterprise-risk-coverage

Candidate Performance Metric record for **Enterprise Risk Coverage** (ERC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-enterprise-risk-coverage`
- **Name:** Enterprise Risk Coverage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ERC

## 2. Definition

A Risk & Compliance indicator, Enterprise Risk Coverage (ERC) quantifies conformance to standards, plans, or obligations. It is computed as Risks with Assigned Owner and Appetite / Total Risks, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The share of the organization's risk universe assessed and managed under the enterprise risk framework - the breadth metric of the ERM program, measuring whether risk management is a comprehensive discipline or a collection of silo assessments. Its strategic significance is completeness: the risk that hurts is disproportionately the one outside the framework - supply-chain, cyber, climate, and third-party exposures historically lived in nobody's register, and coverage is the metric that drives them in. The honest construction enumerates the risk universe first (by business unit and risk category) and then measures assessed share against it, since coverage without a defined universe is a feeling. Read with depth: a program can cover everything shallowly or the material exposures deeply, and the coverage of top-exposure risks by quality assessment is the number that matters for governance.

## Formula

```
Risks with Assigned Owner and Appetite / Total Risks
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** risk_compliance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 383 (batch 1)
