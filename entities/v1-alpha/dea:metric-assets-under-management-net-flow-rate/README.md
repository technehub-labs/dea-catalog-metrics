# dea:metric-assets-under-management-net-flow-rate

Candidate Performance Metric record for **Assets Under Management Net Flow Rate** (AUMNF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-assets-under-management-net-flow-rate`
- **Name:** Assets Under Management Net Flow Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** AUMNF

## 2. Definition

Assets Under Management Net Flow Rate (AUMNF) addresses growth over time and is a fixture of asset & wealth management (deep dive) reporting. The formula is Net New Flows / Opening AUM - reported in percent (%). It is a standard measure in the Financial Services sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures net new AUM (inflows minus outflows) as a share of beginning AUM. Net flows are the organic growth engine of asset management: performance matters, but persistent net outflows shrink fee base regardless of returns, and flow momentum compounds. Separate market movement from flows honestly, and decompose by mandate type and distribution channel. Read with terminated mandate recovery rate and investment performance versus benchmark (Deep Dive).

## Formula

```
Net New Flows / Opening AUM
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** asset_wealth_management_deep_dive
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2102 (batch 6)
