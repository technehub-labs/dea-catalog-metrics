# dea:metric-deal-closure-cycle-time

Candidate Performance Metric record for **Deal Closure Cycle Time** (DCCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-deal-closure-cycle-time`
- **Name:** Deal Closure Cycle Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DCCT

## 2. Definition

Deal Closure Cycle Time (DCCT) addresses how efficiently resources are converted into outputs and is a fixture of investment banking & capital markets reporting. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Days from Mandate to Completion; the result is stated in days. It should be driven down, since lower readings signal healthier performance. In Investment banking, it is a recognized element of the standard performance toolkit.

## 3. Context

Deal closure cycle time measures time from mandate to completion, and in M&A it is the risk-exposure metric of deal execution - long cycles carry more failure risk (market windows close, financing conditions shift, sellers renegotiate), which is why deal-break fees and financing certainty dominate late-stage dynamics. The metric decomposes into diligence length (buyer preparation), regulatory approval duration (antitrust and FDI review timelines have lengthened materially in recent years), and negotiation cadence (momentum matters, and slow processes lose deals to faster buyers). Cycle time by deal type is diagnostic: cross-border deals with regulatory clearances run much longer. Read with deal-completion probability by cycle time (the risk curve), regulatory-approval milestone performance, and diligence-quality issues post-close since compressed diligence transfers risk to integration.

## Formula

```
Days from Mandate to Completion
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_banking_capital_markets
- **Sector:** investment_banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1147 (batch 4)
