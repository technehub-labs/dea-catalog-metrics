# dea:metric-supply-chain-cycle-time

Candidate Performance Metric record for **Supply Chain Cycle Time** (SCCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-supply-chain-cycle-time`
- **Name:** Supply Chain Cycle Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SCCT

## 2. Definition

Supply Chain Cycle Time (SCCT) captures how efficiently resources are converted into outputs for organizations tracking supply chain. The formula is Days to Fulfill Order with Zero Inventory - reported in days. It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

The total time from procuring raw materials to delivering finished goods - the end-to-end velocity of the chain, measured by adding every stage lead time as though inventory were zero between them. Its strategic weight is the connection between time and everything else: cycle time drives the amount of inventory needed to buffer demand uncertainty, so compressing it is the one intervention that simultaneously cuts working capital, improves forecast accuracy (shorter horizons are easier to forecast), and improves service. The zero-inventory convention is what makes it diagnostic - it measures the pure process time without the buffering that hides inefficiency, so the gap between cycle time and actual customer lead time is the inventory the chain is carrying in disguise. The longest stage, not the average stage, is where the leverage is.

## Formula

```
SCCT = Days to Fulfill Order with Zero Inventory
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** supply_chain

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 186 (batch 1)
