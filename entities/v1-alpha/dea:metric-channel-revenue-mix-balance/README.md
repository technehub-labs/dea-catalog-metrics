# dea:metric-channel-revenue-mix-balance

Candidate Performance Metric record for **Channel Revenue Mix Balance** (CRMB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-channel-revenue-mix-balance`
- **Name:** Channel Revenue Mix Balance
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CRMB

## 2. Definition

Channel Revenue Mix Balance (CRMB) addresses exposure to adverse outcomes and is a fixture of channel & distribution management reporting. The formula is Herfindahl-Based Concentration across Channels - reported in index (0-100 or normalized). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the distribution of revenue across channel partners and types. Balance protects against single-partner dependence and channel conflicts. Perfect balance is not the goal: strategic partners should dominate appropriately. Read with channel revenue concentration and direct-to-channel sales ratio.

## Formula

```
Herfindahl-Based Concentration across Channels
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** channel_distribution_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3976 (batch 8)
