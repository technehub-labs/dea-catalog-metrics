# dea:metric-tier-1-capital-ratio

Candidate Performance Metric record for **Tier 1 Capital Ratio** (T1CR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-tier-1-capital-ratio`
- **Name:** Tier 1 Capital Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** T1CR

## 2. Definition

A Banking & Financial Services indicator, Tier 1 Capital Ratio (T1CR) quantifies exposure to adverse outcomes. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Tier 1 Capital / Risk-Weighted Assets, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Financial services.

## 3. Context

Tier 1 capital - common equity plus qualifying instruments that absorb losses going concern - over risk-weighted assets. Within the capital stack, Tier 1 is the loss-bearing layer that keeps a bank alive for shareholders, as opposed to Total capital which counts instruments that only pay out in resolution. Basel III moved the dial decisively toward CET1, its core component, and pushed the quality question further than any prior regime: post-2008 reforms stripped hybrid instruments of their Tier 1 eligibility precisely because they had failed to absorb real losses. The strategic reading is headroom against buffers: the difference between the ratio and the effective requirement including capital buffers - is the bank's capacity to lend, pay dividends, and survive stress simultaneously.

## Formula

```
Tier 1 Capital / Risk-Weighted Assets
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** banking_financial_services
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 40 (batch 1)
