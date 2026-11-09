# dea:metric-reserve-replacement-ratio-deep-dive

Candidate Performance Metric record for **Reserve Replacement Ratio (Deep Dive)** (RRR-M) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-reserve-replacement-ratio-deep-dive`
- **Name:** Reserve Replacement Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RRR-M

## 2. Definition

Reserve Replacement Ratio (Deep Dive) (RRR-M) measures growth over time in the Metals & Mining Operations (Deep Dive) domain. It is computed as New Reserves Added / Reserves Depleted, expressed in ratio (x:1 or x). Its use is concentrated in Metals & Mining. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures additions to reserves against production in the period. Sustained sub-100 percent ratios are the leading indicator of a shrinking company, and reserve quality (grade, depth, permitting) matters as much as quantity. Watch for ratio management through reclassification of resources under looser assumptions late in the period. Read with reserve life trends and finding and development cost.

## Formula

```
RRR-M = New Reserves Added / Reserves Depleted
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** metals_mining_operations_deep_dive
- **Sector:** metals_mining

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1848 (batch 6)
