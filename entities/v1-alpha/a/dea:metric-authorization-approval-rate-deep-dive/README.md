# dea:metric-authorization-approval-rate-deep-dive

Candidate Performance Metric record for **Authorization Approval Rate (Deep Dive)** (AAR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-authorization-approval-rate-deep-dive`
- **Name:** Authorization Approval Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** AAR-D

## 2. Definition

Authorization Approval Rate (Deep Dive) (AAR-D) captures growth over time for organizations tracking payments & cards (deep dive). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Approved Authorizations / Authorization Attempts - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Payments sector.

## 3. Context

Measures the share of card authorizations approved. It is the revenue-enablement metric of payments: every false decline is a completed purchase the issuer killed, with cardholder attrition risk attached. Approval-rate improvements from loosened fraud controls are value-destructive, so the metric must be read jointly with fraud losses. Read with false decline rate (Deep Dive) and card fraud rate basis points.

## Formula

```
AAR-D = Approved Authorizations / Authorization Attempts
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** payments_cards_deep_dive
- **Sector:** payments

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2088 (batch 6)
