# dea:metric-backlog-of-pending-cases

Candidate Performance Metric record for **Backlog of Pending Cases** (BPC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-backlog-of-pending-cases`
- **Name:** Backlog of Pending Cases
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BPC

## 2. Definition

Within Public Sector & Government, Backlog of Pending Cases (BPC) is used to gauge the utilization or availability of capacity. It is defined as Open Cases Aged beyond Service Standard; the result is stated in count (items per period). In Public sector, it is a recognized element of the standard performance toolkit. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the count and age of unresolved cases. It matters because backlog is deferred service debt that compounds citizen frustration and legal risk. Teams can shrink it administratively by closing or archiving stale cases rather than resolving them. Read with Case Processing Time and Reopened Case Rate to confirm backlog reduction reflects resolution, not reclassification.

## Formula

```
Open Cases Aged beyond Service Standard
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** organization
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** public_sector_government
- **Sector:** public_sector

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 636 (batch 2)
