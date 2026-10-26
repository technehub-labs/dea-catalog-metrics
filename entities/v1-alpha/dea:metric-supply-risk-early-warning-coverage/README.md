# dea:metric-supply-risk-early-warning-coverage

Candidate Performance Metric record for **Supply Risk Early Warning Coverage** (SREWC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-supply-risk-early-warning-coverage`
- **Name:** Supply Risk Early Warning Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SREWC

## 2. Definition

Supply Risk Early Warning Coverage (SREWC) addresses exposure to adverse outcomes and is a fixture of strategic sourcing & supplier performance (deep dive) reporting. Its calculation is Critical Suppliers Monitored for Risk Signals / Critical Suppliers, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how completely monitored supply risks have defined triggers and alerts before disruption. Early warning converts supply crises into managed events. Alerts without owner and playbook response are noise. Read with supply chain risk event detection rate and horizon scan coverage ratio.

## Formula

```
Critical Suppliers Monitored for Risk Signals / Critical Suppliers
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** strategic_sourcing_supplier_performance_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3750 (batch 8)
