# dea:metric-counterparty-exposure-limit-utilization-deep-dive

Candidate Performance Metric record for **Counterparty Exposure Limit Utilization (Deep Dive)** (CELU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-counterparty-exposure-limit-utilization-deep-dive`
- **Name:** Counterparty Exposure Limit Utilization (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CELU

## 2. Definition

Counterparty Exposure Limit Utilization (Deep Dive) (CELU) addresses exposure to adverse outcomes and is a fixture of corporate treasury (deep dive) reporting. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Exposure to Counterparty / Approved Limit - reported in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures usage of credit limits against approved counterparty ceilings. It is the concentration-risk dial of treasury: utilization persistently near limits signals either under-sized limits or genuine risk appetite breach, and both deserve attention. Exposure measurement net of collateral is the honest read, since gross utilization overstates risk where security exists. Read with counterparty credit ratings drift and stress-scenario exposures.

## Formula

```
CELU = Exposure to Counterparty / Approved Limit
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** corporate_treasury_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2185 (batch 6)
