# dea:metric-concentration-by-counterparty-deep-dive

Candidate Performance Metric record for **Concentration by Counterparty (Deep Dive)** (CBCDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-concentration-by-counterparty-deep-dive`
- **Name:** Concentration by Counterparty (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CBCDD

## 2. Definition

Concentration by Counterparty (Deep Dive) (CBCDD) addresses exposure to adverse outcomes and is a fixture of credit & collections risk (enterprise) reporting. Its calculation is Largest Exposure / Total Credit Exposure, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures exposure concentration across obligors. Concentrated books convert single defaults into portfolio events. Exposure netted against optimistic collateral overstates diversification. Read with counterparty exposure concentration and concentration risk ratio.

## Formula

```
CBCDD = Largest Exposure / Total Credit Exposure
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** credit_collections_risk_enterprise

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4208 (batch 9)
