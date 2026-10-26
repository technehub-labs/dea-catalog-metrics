# dea:metric-churn-rate-telecom

Candidate Performance Metric record for **Churn Rate (Telecom)** (CR-T) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-churn-rate-telecom`
- **Name:** Churn Rate (Telecom)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CR-T

## 2. Definition

Churn Rate (Telecom) (CR-T) measures exposure to adverse outcomes in the Telecommunications domain. It is computed as Subscribers Lost / Average Subscribers, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is concentrated in Telecommunications.

## 3. Context

The share of subscribers lost over a period - the retention metric of the connectivity business, where the model has three structural features that make churn central: acquisition cost is high, switching has friction (device financing, bundling, network loyalty), and mature markets are zero-sum, so every retained customer is a customer a competitor did not acquire. Its strategic significance is the bundling economics: operators converged on multi-service bundles precisely because bundle churn runs far below single-service churn, and the metric is the quiet justification for every convergence strategy in the sector. Read by segment and reason: postpaid churn behaves differently from prepaid, and involuntary churn (device-repayment default) is a credit-risk signal rather than a satisfaction one. In a saturated market, churn is effectively the growth metric.

## Formula

```
Subscribers Lost / Average Subscribers
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** telecommunications
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 525 (batch 1)
