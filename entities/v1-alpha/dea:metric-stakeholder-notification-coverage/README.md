# dea:metric-stakeholder-notification-coverage

Candidate Performance Metric record for **Stakeholder Notification Coverage** (SNC-CM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-stakeholder-notification-coverage`
- **Name:** Stakeholder Notification Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SNC-CM

## 2. Definition

Stakeholder Notification Coverage (SNC-CM) measures conformance to standards, plans, or obligations in the Crisis Management & Emergency Response domain. The formula is Priority Stakeholders Notified within Threshold / Stakeholders - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures whether all required stakeholders (regulators, customers, employees, partners) are notified within required windows. Notification failures create legal exposure on top of the crisis itself. Coverage without contact-data currency fails at the worst moment. Read with privacy breach notification timeliness and crisis communication approval cycle time.

## Formula

```
SNC-CM = Priority Stakeholders Notified within Threshold / Stakeholders
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
- **Domain:** crisis_management_emergency_response

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3538 (batch 8)
