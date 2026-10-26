# dea:metric-compliance-breach-count

Candidate Performance Metric record for **Compliance Breach Count** (CBC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-compliance-breach-count`
- **Name:** Compliance Breach Count
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CBC

## 2. Definition

A Risk & Compliance indicator, Compliance Breach Count (CBC) quantifies exposure to adverse outcomes. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Confirmed Regulatory Breaches per Period, measured in count (items per period). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The number of incidents where the organization failed to meet a regulatory or legal obligation - the raw event count of the compliance function, distinguished from near-misses and control weaknesses by the fact that a duty was actually missed. Its strategic weight is consequence asymmetry: a single breach in a heavily regulated domain (AML, data protection, safety) can carry penalties, license consequences, and monitorships that dwarf the compliance budget, which is why boards treat any nonzero count as requiring explanation rather than trending. The analytic work is concentration: breaches clustered in one process indicate a system defect, scattered breaches indicate a culture or complexity problem, and the two demand opposite responses. Rising counts after monitoring investment reflect detection maturity, exactly as in security - the base rate of undetected noncompliance is unknowable, and honesty about that distinguishes mature reporting.

## Formula

```
Confirmed Regulatory Breaches per Period
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 377 (batch 1)
