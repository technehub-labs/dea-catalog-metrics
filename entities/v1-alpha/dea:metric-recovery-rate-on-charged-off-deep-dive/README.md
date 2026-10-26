# dea:metric-recovery-rate-on-charged-off-deep-dive

Candidate Performance Metric record for **Recovery Rate on Charged-Off (Deep Dive)** (RRCOD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-recovery-rate-on-charged-off-deep-dive`
- **Name:** Recovery Rate on Charged-Off (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RRCOD

## 2. Definition

Recovery Rate on Charged-Off (Deep Dive) (RRCOD) captures the economic value created or preserved for organizations tracking credit & collections risk (enterprise). The formula is Recovered Amount / Charged-Off Amount - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how much of charged-off balances are eventually recovered. Recovery converts gross charge-offs into net losses. Recovery on old, worked-out books differs enormously from fresh charge-offs. Read with loss given default (Deep Dive) and collections effectiveness index.

## Formula

```
Recovered Amount / Charged-Off Amount
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** credit_collections_risk_enterprise

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4203 (batch 9)
