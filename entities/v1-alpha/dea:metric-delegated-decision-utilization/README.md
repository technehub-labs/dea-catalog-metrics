# dea:metric-delegated-decision-utilization

Candidate Performance Metric record for **Delegated Decision Utilization** (DDU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-delegated-decision-utilization`
- **Name:** Delegated Decision Utilization
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DDU

## 2. Definition

Delegated Decision Utilization (DDU) addresses capability maturity or development and is a fixture of operating model & decision effectiveness reporting. The formula is Decisions Taken at Delegated Level / Decisions Eligible - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how often decisions are actually taken at the delegated level versus escalated upward, revealing whether empowerment is real or nominal. Chronic under-utilization signals either unclear decision rights, capability gaps, or a culture that punishes autonomous error - each needing a different fix. Be alert to gaming via nominal sign-off after the real decision has been pre-cleared, and to escalation that is simply delegation of blame. Read with span of control and decision cycle time.

## Formula

```
Decisions Taken at Delegated Level / Decisions Eligible
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** capability
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** operating_model_decision_effectiveness

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1301 (batch 5)
