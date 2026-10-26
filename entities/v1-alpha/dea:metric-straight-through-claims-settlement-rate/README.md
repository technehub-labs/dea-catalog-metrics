# dea:metric-straight-through-claims-settlement-rate

Candidate Performance Metric record for **Straight-Through Claims Settlement Rate** (STCS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-straight-through-claims-settlement-rate`
- **Name:** Straight-Through Claims Settlement Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** STCS

## 2. Definition

Within Insurance Claims Deep Dive, Straight-Through Claims Settlement Rate (STCS) is used to gauge how efficiently resources are converted into outputs. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Claims Settled without Human Touch / Claims; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. In Insurance, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the share of claims settled end-to-end without manual handling. It is the efficiency frontier of claims transformation, and it is only as good as the routing rules: complex claims forced through STP create rework and angry customers, while generous manual referral thresholds quietly hollow the number. Report alongside accuracy and reopen rates by settlement path. Read with claim decision automation rate and leakage by path.

## Formula

```
STCS = Claims Settled without Human Touch / Claims
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_claims_deep_dive
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1548 (batch 6)
