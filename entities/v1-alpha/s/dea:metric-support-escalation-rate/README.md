# dea:metric-support-escalation-rate

Candidate Performance Metric record for **Support Escalation Rate** (SER-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-support-escalation-rate`
- **Name:** Support Escalation Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SER-S

## 2. Definition

Support Escalation Rate (SER-S) addresses exposure to adverse outcomes and is a fixture of customer success (b2b saas) reporting. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Escalated Tickets / Total Tickets, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Software & SaaS.

## Formula

```
SER-S = Escalated Tickets / Total Tickets
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** customer_success_b2b_saas
- **Sector:** software_saas

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 591 (batch 2)
