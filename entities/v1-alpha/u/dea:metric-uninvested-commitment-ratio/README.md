# dea:metric-uninvested-commitment-ratio

Candidate Performance Metric record for **Uninvested Commitment Ratio** (UCR-IM2) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-uninvested-commitment-ratio`
- **Name:** Uninvested Commitment Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** UCR-IM2

## 2. Definition

Uninvested Commitment Ratio (UCR-IM2) measures the utilization or availability of capacity in the Investment Management - Portfolio Operations domain. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Uncalled Capital / Total Commitments (Private) - reported in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. It is a standard measure in the Financial Services sector.

## 3. Context

Measures dry-powder capital not yet deployed against total committed. Persistent high uninvested balances signal sourcing problems or deployment discipline, and invite LP pressure. Slow deployment in a competitive market means adverse selection into the leftover deals. Read with dry powder coverage ratio and distribution-to-paid-in ratio (Private).

## Formula

```
UCR-IM2 = Uncalled Capital / Total Commitments (Private)
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_management_portfolio_operations
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3018 (batch 7)
