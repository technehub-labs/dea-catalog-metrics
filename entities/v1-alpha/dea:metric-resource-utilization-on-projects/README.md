# dea:metric-resource-utilization-on-projects

Candidate Performance Metric record for **Resource Utilization on Projects** (RUP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-resource-utilization-on-projects`
- **Name:** Resource Utilization on Projects
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RUP

## 2. Definition

Resource Utilization on Projects (RUP) captures the utilization or availability of capacity for organizations tracking project management. The formula is Billable or Project Hours / Available Hours - reported in percent (%). It is applied across virtually every sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures how much of project team capacity is spent on project work versus idle or diverted time. It matters because billable and delivery economics collapse when utilization drifts low. Chasing utilization can push people onto low-value tasks just to look busy. Read with Project Margin and Schedule Performance Index to ensure utilization targets support delivery rather than vanity.

## Formula

```
Billable or Project Hours / Available Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** transformation
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** project_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 359 (batch 1)
