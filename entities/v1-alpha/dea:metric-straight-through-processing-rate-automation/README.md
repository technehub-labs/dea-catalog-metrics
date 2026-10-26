# dea:metric-straight-through-processing-rate-automation

Candidate Performance Metric record for **Straight-Through Processing Rate (Automation)** (STPA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-straight-through-processing-rate-automation`
- **Name:** Straight-Through Processing Rate (Automation)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** STPA

## 2. Definition

Straight-Through Processing Rate (Automation) (STPA) addresses how efficiently resources are converted into outputs and is a fixture of automation & robotic process automation reporting. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Transactions Processed End-to-End without Manual Touch / Transactions - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of transactions or cases completed end-to-end without human touch. It is the purest efficiency measure of automation maturity because every exception route is a cost and usually a delay. Honest reads separate true STP from silent exception queues, and from human pre-processing done upstream to keep cases clean. Segment by case type, since blended rates hide high-value complex work that resists automation. Read with exception handling cost and process automation coverage.

## Formula

```
Transactions Processed End-to-End without Manual Touch / Transactions
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1326 (batch 5)
