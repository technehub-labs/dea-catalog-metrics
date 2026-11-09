# dea:metric-regulatory-finding-closure-time

Candidate Performance Metric record for **Regulatory Finding Closure Time** (RFCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-regulatory-finding-closure-time`
- **Name:** Regulatory Finding Closure Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RFCT

## 2. Definition

Regulatory Finding Closure Time (RFCT) addresses conformance to standards, plans, or obligations and is a fixture of risk & compliance reporting. Its calculation is Days from Finding to Verified Closure, measured in days. It is applied across virtually every sector. Its value drives prioritization and resource reallocation among competing initiatives. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures average time from regulatory finding to verified closure. It matters because open findings compound scrutiny, fines, and consent-order risk. Teams can close on paper with weak evidence, gambling that the next exam does not re-test. Read with Audit Nonconformance Closure Rate and repeat-finding trends to confirm closures withstand re-examination.

## Formula

```
RFCT = Days from Finding to Verified Closure
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 378 (batch 1)
