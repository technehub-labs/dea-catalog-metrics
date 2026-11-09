# dea:metric-first-call-resolution-deep-dive

Candidate Performance Metric record for **First Call Resolution (Deep Dive)** (FCR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-first-call-resolution-deep-dive`
- **Name:** First Call Resolution (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FCR-D

## 2. Definition

A Contact Center Operations (Deep Dive) indicator, First Call Resolution (Deep Dive) (FCR-D) quantifies the quality of outputs and outcomes. The formula is Resolved on First Contact / Total Contacts - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures contacts resolved without repeat contact or transfer. It is the efficiency-experience convergence metric: repeat contacts double cost and halve satisfaction, and FCR is the single strongest operational predictor of both. Measurement integrity is the challenge - resolved must be verified by the customer's absence of follow-up, not the agent's disposition coding, which is routinely optimistic. Read with repeat-contact rate within seven days and transfer patterns.

## Formula

```
FCR-D = Resolved on First Contact / Total Contacts
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contact_center_operations_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2479 (batch 6)
