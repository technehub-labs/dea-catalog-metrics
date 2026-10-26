# dea:metric-regulatory-penalty-exposure

Candidate Performance Metric record for **Regulatory Penalty Exposure** (RPE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-regulatory-penalty-exposure`
- **Name:** Regulatory Penalty Exposure
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RPE

## 2. Definition

Regulatory Penalty Exposure (RPE) measures exposure to adverse outcomes in the Legal domain. It is computed as Sum of Potential Penalties from Open Matters, expressed in currency value. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

The quantified potential penalty burden from current regulatory matters and identified noncompliance - the forward-looking ledger that legal and compliance functions maintain to make exposure comparable with the other demands on capital and attention. Its strategic weight is planning: potential penalties for open matters become provisioning questions for finance and disclosure questions for investor relations, and a rigorous exposure estimate is what separates the firms that guide the market from the firms that surprise it. The estimation honesty problem is the difference between statutory maxima and realistic outcomes - maxima are arithmetic, outcomes are negotiated - so credible exposure models use enforcement-history base rates for the regime and violation class. Read with trend: rising exposure on unresolved matters ages badly, since penalty expectations compound as matters mature.

## Formula

```
Sum of Potential Penalties from Open Matters
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** legal

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 394 (batch 1)
