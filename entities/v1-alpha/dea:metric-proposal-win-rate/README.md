# dea:metric-proposal-win-rate

Candidate Performance Metric record for **Proposal Win Rate** (PWR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-proposal-win-rate`
- **Name:** Proposal Win Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PWR

## 2. Definition

Within Professional Services, Proposal Win Rate (PWR) is used to gauge growth over time. It is computed as Proposals Won / Proposals Submitted, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Professional services.

## 3. Context

Proposals won as a share submitted - the conversion metric of the professional-services sales process, and one with an economics of its own: proposals are expensive (partner time, solutioning, pricing workshops), so win rate against cost-to-propose determines whether the pursuit pipeline is affordable. The strategic significance is the selectivity question: firms that respond to everything show low win rates and high pursuit costs; firms that qualify hard show high win rates at the risk of insufficient pipeline - and the deliberate position on that curve is the strategy. The honest analysis is by pursuit type: sole-source renewals, competitive finals, and long-list requests-for-proposal have entirely different base rates, and a blended win rate moves with pursuit mix more than with capability. Read with the no-bid discipline: the share of opportunities declined at qualification is the upstream decision that determines the win rate more than any selling skill does.

## Formula

```
Proposals Won / Proposals Submitted
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** professional_services
- **Sector:** professional_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 685 (batch 2)
