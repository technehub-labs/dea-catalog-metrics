# dea:metric-continuity-plan-currency-score

Candidate Performance Metric record for **Continuity Plan Currency Score** (CPCC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-continuity-plan-currency-score`
- **Name:** Continuity Plan Currency Score
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CPCC

## 2. Definition

A Business Continuity & Disaster Recovery indicator, Continuity Plan Currency Score (CPCC) quantifies the quality of outputs and outcomes. It is computed as BCPs Updated within 12 Months and Version-Controlled / BCPs, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures whether continuity plans reflect the current organization, technology, and people. Plans decay silently between updates as everything around them changes. Currency measured as review date rather than tested substance is hygiene. Read with business continuity plan coverage (Deep Dive) and business impact analysis currency.

## Formula

```
CPCC = BCPs Updated within 12 Months and Version-Controlled / BCPs
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** business_continuity_disaster_recovery

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3534 (batch 8)
