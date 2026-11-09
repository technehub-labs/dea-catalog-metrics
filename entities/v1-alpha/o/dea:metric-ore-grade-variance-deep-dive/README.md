# dea:metric-ore-grade-variance-deep-dive

Candidate Performance Metric record for **Ore Grade Variance (Deep Dive)** (OGV-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ore-grade-variance-deep-dive`
- **Name:** Ore Grade Variance (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** OGV-D

## 2. Definition

Within Metals & Mining Operations (Deep Dive), Ore Grade Variance (Deep Dive) (OGV-D) is used to gauge the quality of outputs and outcomes. Its calculation is Milled Grade - Resource Model Grade / Model Grade, measured in percent (%). It originates from and is most used in Metals & Mining practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures deviation between actual ore grade and the resource model as mining progresses. Grade variance is the transmission channel between geology and economics: persistent negative variance destroys mine plans, reserve estimates, and mill feed economics simultaneously. Reconciliation discipline (mine-to-mill) makes the variance actionable rather than forensic. Read with metal recovery rate (Deep Dive) and reserve model update cadence.

## Formula

```
OGV-D = Milled Grade - Resource Model Grade / Model Grade
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** metals_mining_operations_deep_dive
- **Sector:** metals_mining

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1838 (batch 6)
