# dea:metric-decision-cycle-time

Candidate Performance Metric record for **Decision Cycle Time** (DCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-decision-cycle-time`
- **Name:** Decision Cycle Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DCT

## 2. Definition

A Operating Model & Decision Effectiveness indicator, Decision Cycle Time (DCT) quantifies how efficiently resources are converted into outputs. The formula is Days from Decision Request to Approved Decision - reported in days. It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the elapsed time from when a decision is needed to when it is made at the right level, a direct probe of organizational friction. Slow decisions are often more expensive than wrong-but-correctable ones in fast markets, which is why this belongs on a strategy scorecard. Honest measurement requires clear decision timestamps, which most companies lack, so proxies (meeting cycles, approval chains) must be validated before trusting trendlines. Read with delegated decision utilization and time loss to bureaucracy.

## Formula

```
DCT = Days from Decision Request to Approved Decision
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** organization
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** operating_model_decision_effectiveness

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1300 (batch 5)
