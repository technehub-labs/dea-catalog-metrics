# dea:metric-entity-level-control-coverage

Candidate Performance Metric record for **Entity-Level Control Coverage** (ELCC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-entity-level-control-coverage`
- **Name:** Entity-Level Control Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ELCC

## 2. Definition

A Internal Controls & Financial Reporting Integrity indicator, Entity-Level Control Coverage (ELCC) quantifies conformance to standards, plans, or obligations. Its calculation is Entities with Documented Entity-Level Controls / Entities, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how thoroughly entity-level controls (governance, ethics, delegation, oversight) cover the organization. Entity-level controls set the tone that application controls inherit. Coverage counted as policy existence rather than operating evidence is nominal. Read with three lines model compliance score and control environment maturity score.

## Formula

```
ELCC = Entities with Documented Entity-Level Controls / Entities
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
- **Domain:** internal_controls_financial_reporting_integrity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3591 (batch 8)
