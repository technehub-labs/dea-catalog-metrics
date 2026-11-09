# dea:metric-risk-mitigation-progress

Candidate Performance Metric record for **Risk Mitigation Progress** (RMP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-risk-mitigation-progress`
- **Name:** Risk Mitigation Progress
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RMP

## 2. Definition

Risk Mitigation Progress (RMP) measures conformance to standards, plans, or obligations in the Risk & Compliance domain. Its calculation is Mitigation Actions Completed / Mitigation Actions Planned, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The share of planned mitigation actions completed on schedule - the execution metric of the risk program, tracking whether identified risks are being treated or merely catalogued. Its strategic weight is the gap it measures: risk registers are famously populated with mitigations that live forever in planning, and this metric converts that pathology into a visible backlog with aging. The honest construction weights actions by the exposure they address - completing 95 percent of trivial mitigations while the top-exposure items age is compliance theater - so mature programs report progress weighted by risk value and include aging of overdue items. Read against the risk dashboard itself: mitigation progress rising while exposure stays flat indicates the actions are not working, which is the more consequential finding the activity metric cannot see.

## Formula

```
RMP = Mitigation Actions Completed / Mitigation Actions Planned
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
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** risk_compliance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 375 (batch 1)
