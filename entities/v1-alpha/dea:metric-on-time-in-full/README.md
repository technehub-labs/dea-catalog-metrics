# dea:metric-on-time-in-full

Candidate Performance Metric record for **On-Time In-Full** (OTIF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-on-time-in-full`
- **Name:** On-Time In-Full
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** OTIF

## 2. Definition

On-Time In-Full (OTIF) addresses the quality of outputs and outcomes and is a fixture of supply chain reporting. It is computed as Orders Delivered On Time and Complete / Total Orders, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The share of order lines delivered complete and on the customer-requested date - the fulfillment metric that has become the de facto service standard in retail supplier scorecards, where major grocers attach chargebacks and volume guarantees to it. Its strategic weight is contractual: OTIF misses carry direct penalties in many retail relationships, and chronic misses shrink allocations in the next range review, so the metric is simultaneously an operational measure and a commercial asset. The distinction from perfect order rate is scope - OTIF focuses on time and completeness, not damage and documentation - which makes it simpler to automate and easier to game (through buffer-padding promised dates). The honest version measures against the date the customer originally requested, not the date the system eventually confirmed.

## Formula

```
OTIF = Orders Delivered On Time and Complete / Total Orders
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** supply_chain

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 174 (batch 1)
