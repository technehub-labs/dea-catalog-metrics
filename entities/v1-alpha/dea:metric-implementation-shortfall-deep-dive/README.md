# dea:metric-implementation-shortfall-deep-dive

Candidate Performance Metric record for **Implementation Shortfall (Deep Dive)** (ISF-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-implementation-shortfall-deep-dive`
- **Name:** Implementation Shortfall (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ISF-D

## 2. Definition

Implementation Shortfall (Deep Dive) (ISF-D) captures how efficiently resources are converted into outputs for organizations tracking investment research & trading operations. It is computed as Realized versus Paper Portfolio Cost, expressed in percent (%). Its use is concentrated in Financial Services. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the total cost of executing an order versus the decision price, including delay, spread, and market impact. Shortfall is the honest all-in price of trading: it reveals whether investment alpha survives execution. Attribution that lumps all slippage into 'market' excuses avoidable delay costs. Read with TCA coverage of orders and best execution compliance rate.

## Formula

```
Realized versus Paper Portfolio Cost
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_research_trading_operations
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3037 (batch 7)
