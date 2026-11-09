# dea:metric-regulatory-change-response-time

Candidate Performance Metric record for **Regulatory Change Response Time** (RCRT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-regulatory-change-response-time`
- **Name:** Regulatory Change Response Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RCRT

## 2. Definition

Regulatory Change Response Time (RCRT) captures conformance to standards, plans, or obligations for organizations tracking risk & compliance. It is defined as Days from Regulatory Publication to Compliance Action; the result is stated in days. It is applied across virtually every sector. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures time from regulatory change publication to implemented compliance response. It matters because late adaptation creates a window of violation exposure. It can be gamed by declaring interim manual controls as implementation while systems lag. Read with Regulatory Finding Closure Time and Compliance Training completion to check responses are operational, not nominal.

## Formula

```
RCRT = Days from Regulatory Publication to Compliance Action
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** risk_compliance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 381 (batch 1)
