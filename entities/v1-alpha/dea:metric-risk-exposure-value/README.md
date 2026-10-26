# dea:metric-risk-exposure-value

Candidate Performance Metric record for **Risk Exposure Value** (REV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-risk-exposure-value`
- **Name:** Risk Exposure Value
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** REV

## 2. Definition

Risk Exposure Value (REV) measures exposure to adverse outcomes in the Risk & Compliance domain. Its calculation is Sum of (Likelihood x Impact) across Key Risks, measured in currency value. It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

The monetary quantification of exposure across risks - conventionally expected loss (probability times impact) aggregated, or better, the tail metrics that the risk-management profession increasingly prefers. Its strategic weight is that it makes risk commensurable with strategy: an exposure expressed in currency can be compared against capital, earnings, and the cost of mitigation, which is what moves risk from a compliance register into resource allocation. The measurement honesty problem is the fat tail - expected loss understates catastrophe-heavy risk profiles, which is why value-at-risk and conditional tail expectations entered the toolkit, and why a single exposure number must always travel with its distribution. Read with appetite: exposure against stated tolerance is the governance conversation, exposure in the abstract is an inventory.

## Formula

```
Sum of (Likelihood x Impact) across Key Risks
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** risk_compliance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 374 (batch 1)
