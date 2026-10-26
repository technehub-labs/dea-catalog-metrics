# dea:metric-continuity-plan-activation-success-rate

Candidate Performance Metric record for **Continuity Plan Activation Success Rate** (CPASR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-continuity-plan-activation-success-rate`
- **Name:** Continuity Plan Activation Success Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CPASR

## 2. Definition

Continuity Plan Activation Success Rate (CPASR) addresses exposure to adverse outcomes and is a fixture of business continuity & disaster recovery reporting. It is defined as Activations Executed per Plan without Failure / Activations; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures whether plan activations (real or simulated) restore operations as designed. Real activations are the ultimate test of the entire program. Success judged on partial restoration hides the failed components. Read with disaster recovery test pass rate and business downtime per crisis event.

## Formula

```
Activations Executed per Plan without Failure / Activations
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3523 (batch 8)
