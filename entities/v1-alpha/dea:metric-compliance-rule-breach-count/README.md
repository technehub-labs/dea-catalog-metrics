# dea:metric-compliance-rule-breach-count

Candidate Performance Metric record for **Compliance Rule Breach Count** (CRBC-IR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-compliance-rule-breach-count`
- **Name:** Compliance Rule Breach Count
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CRBC-IR

## 2. Definition

Compliance Rule Breach Count (CRBC-IR) captures conformance to standards, plans, or obligations for organizations tracking investment risk & middle office operations. The formula is Mandate Rule Breaches in Period - reported in count (items per period). It is a standard measure in the Investment management sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the number of investment compliance rule breaches in the period. Breaches are the audit trail of whether the compliance framework actually constrains behavior. Counts without severity classification inflate small breaches or hide large ones. Read with mandate compliance breach count and compliance rule coverage.

## Formula

```
Mandate Rule Breaches in Period
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** financial
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_risk_middle_office_operations
- **Sector:** investment_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3470 (batch 7)
