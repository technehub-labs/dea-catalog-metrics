# dea:metric-finished-goods-availability

Candidate Performance Metric record for **Finished Goods Availability** (FGA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-finished-goods-availability`
- **Name:** Finished Goods Availability
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FGA

## 2. Definition

Finished Goods Availability (FGA) addresses the utilization or availability of capacity and is a fixture of sales & operations planning reporting. The formula is Demand Lines Fulfilled from Stock / Demand Lines - reported in percent (%). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of finished goods demand met from stock at the moment of need. It matters because FG availability is the final S&OP promise to the customer. Availability can be gamed by measuring at DC level while customer-facing orders fail. Read with Fill Rate at order level and Backorder Rate to confirm availability is customer-felt.

## Formula

```
FGA = Demand Lines Fulfilled from Stock / Demand Lines
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sales_operations_planning

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1297 (batch 5)
