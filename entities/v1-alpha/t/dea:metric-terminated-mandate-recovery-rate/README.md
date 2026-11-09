# dea:metric-terminated-mandate-recovery-rate

Candidate Performance Metric record for **Terminated Mandate Recovery Rate** (TMRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-terminated-mandate-recovery-rate`
- **Name:** Terminated Mandate Recovery Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TMRR

## 2. Definition

A Asset & Wealth Management (Deep Dive) indicator, Terminated Mandate Recovery Rate (TMRR) quantifies the retention of customers, users, or assets over time. It is computed as Won-Back Mandates / Terminated Mandates, expressed in percent (%). Its use is concentrated in Financial Services. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of lost mandates subsequently won back. Institutional asset management is a small-world market: mandate losses are public, and recovery both restores fee base and signals whether the underlying issues were fixed. Recovery won through fee concessions can be value-negative for the firm, so read pricing on recovered mandates. Read with loss-reason analysis and investment performance versus benchmark (Deep Dive) for the causal chain.

## Formula

```
TMRR = Won-Back Mandates / Terminated Mandates
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** retention
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2112 (batch 6)
