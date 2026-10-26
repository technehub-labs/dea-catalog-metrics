# dea:metric-exception-approval-rate-at-governance

Candidate Performance Metric record for **Exception Approval Rate at Governance** (EARG) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-exception-approval-rate-at-governance`
- **Name:** Exception Approval Rate at Governance
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** EARG

## 2. Definition

Exception Approval Rate at Governance (EARG) measures conformance to standards, plans, or obligations in the Enterprise Decision Effectiveness & Governance Monitoring domain. The formula is Items Approved with Exceptions / Items Reviewed - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the share of items arriving at governance bodies seeking exceptions to standard policy. High exception rates signal policies that don't fit reality or a culture of negotiated bypass. Exceptions approved near-universally indicate the rule, not the exception, has moved. Read with stage gate bypass rate and delegation of authority compliance.

## Formula

```
Items Approved with Exceptions / Items Reviewed
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** enterprise_decision_effectiveness_governance_monitoring

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3143 (batch 7)
