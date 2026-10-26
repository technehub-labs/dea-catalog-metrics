# dea:metric-unplanned-unit-downtime-refining

Candidate Performance Metric record for **Unplanned Unit Downtime (Refining)** (UUDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-unplanned-unit-downtime-refining`
- **Name:** Unplanned Unit Downtime (Refining)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** UUDR

## 2. Definition

Within Oil & Gas Downstream & Refining, Unplanned Unit Downtime (Refining) (UUDR) is used to gauge exposure to adverse outcomes. Its calculation is Unplanned Downtime / Operating Period, measured in percent (%). It originates from and is most used in Oil & Gas practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures unplanned outages of process units. In refining, unplanned downtime converts margin directly - downed units still carry fixed cost while missing the crack - and it is usually the largest controllable profit swing. Root-cause distribution (equipment failure versus operational error versus fouling) directs investment. Read with asset mechanical integrity compliance and turnaround execution quality.

## Formula

```
Unplanned Downtime / Operating Period
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** oil_gas_downstream_refining
- **Sector:** oil_gas

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2300 (batch 6)
