# dea:metric-delegation-of-authority-compliance

Candidate Performance Metric record for **Delegation of Authority Compliance** (DOAC-GOV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-delegation-of-authority-compliance`
- **Name:** Delegation of Authority Compliance
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DOAC-GOV

## 2. Definition

Delegation of Authority Compliance (DOAC-GOV) measures conformance to standards, plans, or obligations in the Enterprise Decision Effectiveness & Governance Monitoring domain. Its calculation is Decisions within Approved Authority / Sampled Decisions, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures adherence to the approved authority matrix in commitments and spend. DoA violations are the audit trail of governance erosion. Compliance through retrospective ratification (approving after the fact) is violation with paperwork. Read with decision right first time rate and exception approval rate at governance.

## Formula

```
Decisions within Approved Authority / Sampled Decisions
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
- **Domain:** enterprise_decision_effectiveness_governance_monitoring

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3139 (batch 7)
