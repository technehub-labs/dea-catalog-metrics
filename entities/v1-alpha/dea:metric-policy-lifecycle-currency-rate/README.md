# dea:metric-policy-lifecycle-currency-rate

Candidate Performance Metric record for **Policy Lifecycle Currency Rate** (PLCR-GOV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-policy-lifecycle-currency-rate`
- **Name:** Policy Lifecycle Currency Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PLCR-GOV

## 2. Definition

Policy Lifecycle Currency Rate (PLCR-GOV) addresses conformance to standards, plans, or obligations and is a fixture of enterprise decision effectiveness & governance monitoring reporting. The formula is Policies Reviewed within Cycle / Policies - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures whether policies are within their review cycles and reflect current regulation and operating reality. A policy estate nobody maintains is an estate nobody follows. Currency measured as date-stamp rather than substance review is thin. Read with policy exception rate and regulatory change adoption timeliness.

## Formula

```
PLCR-GOV = Policies Reviewed within Cycle / Policies
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
- **Domain:** enterprise_decision_effectiveness_governance_monitoring

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3148 (batch 7)
