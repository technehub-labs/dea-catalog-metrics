# dea:metric-contract-fill-ratio-temporary

Candidate Performance Metric record for **Contract Fill Ratio (Temporary)** (CFRT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-contract-fill-ratio-temporary`
- **Name:** Contract Fill Ratio (Temporary)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CFRT

## 2. Definition

Contract Fill Ratio (Temporary) (CFRT) captures the utilization or availability of capacity for organizations tracking staffing & recruiting. It is defined as Contract Requirements Filled / Contract Openings; the result is stated in percent (%). In Staffing & recruiting, it is a recognized element of the standard performance toolkit. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of temporary staffing requisitions filled within the requested timeframe. It matters because temp fill reliability is the core service promise in staffing. Fill can be inflated by lowering candidate quality bar under time pressure. Read with Client Satisfaction and Early Termination of Placements to confirm filled contracts meet expectations.

## Formula

```
CFRT = Contract Requirements Filled / Contract Openings
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** staffing_recruiting
- **Sector:** staffing_recruiting

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1024 (batch 3)
