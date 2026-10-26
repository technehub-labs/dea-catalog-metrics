# dea:metric-savings-realization-rate

Candidate Performance Metric record for **Savings Realization Rate** (SRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-savings-realization-rate`
- **Name:** Savings Realization Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SRR

## 2. Definition

Savings Realization Rate (SRR) addresses the economic value created or preserved and is a fixture of procurement reporting. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Realized Savings / Identified Savings, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The share of negotiated savings that actually reaches the P&L - the honesty metric of procurement, because a negotiated price reduction only becomes money when volume actually buys at the new price, specifications do not creep back, and the demand does not simply expand to consume the saving. Realization rates below 80 percent are common, which is why finance departments increasingly refuse to credit procurement for negotiated numbers and insist on this one. Strategic use is the credibility bridge: procurement organizations that report realized savings against a baseline method agree with the CFO become partners, while those reporting negotiated numbers remain vendors of good news. The methodological battleground is the baseline - should-cost, market index, or last-price-paid all produce different savings on the same deal - so the convention must be fixed before the number means anything.

## Formula

```
Realized Savings / Identified Savings
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** procurement

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 228 (batch 1)
