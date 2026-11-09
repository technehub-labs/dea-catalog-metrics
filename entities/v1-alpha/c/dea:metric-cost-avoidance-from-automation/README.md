# dea:metric-cost-avoidance-from-automation

Candidate Performance Metric record for **Cost Avoidance from Automation** (CAA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-avoidance-from-automation`
- **Name:** Cost Avoidance from Automation
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CAA

## 2. Definition

Cost Avoidance from Automation (CAA) addresses the economic value created or preserved and is a fixture of automation & robotic process automation reporting. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Manual Cost Avoided through Automation, Annualized, expressed in currency value. Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Quantifies spending that would have occurred absent automation - capacity not hired, overtime not paid, error rework eliminated. It is a legitimate but easily inflated metric: counterfactual baselines grow conveniently, and avoided cost never appears in a budget line to verify. Tie every avoidance claim to an operational counterfactual (cost per case times volume growth) and reconcile periodically with realized run-rate savings. Read with automation payback period and cost reduction program realization.

## Formula

```
CAA = Manual Cost Avoided through Automation, Annualized
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** automation_robotic_process_automation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1327 (batch 5)
