# dea:metric-net-collection-rate

Candidate Performance Metric record for **Net Collection Rate** (NCR-H) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-net-collection-rate`
- **Name:** Net Collection Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** NCR-H

## 2. Definition

A Healthcare Revenue Cycle indicator, Net Collection Rate (NCR-H) quantifies the economic value created or preserved. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Payments Received / Charges Billable at Contracted Rates - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Healthcare sector.

## 3. Context

Net collection rate measures the share of billable value actually collected after contractual adjustments, denials, and write-offs, and it is the difference between healthcare's paper prices and real economics - a practice can show strong gross revenue while collecting a fraction of it, and net collection rate exposes that gap directly. It is the revenue-integrity metric: every point of collection improvement drops straight to margin without adding a single patient encounter. The measurement discipline is denominator care - collections divided by charges is meaningless when charge master prices are inflated several-fold above expected payment, so the honest version collects against contractually expected amounts. Read with denial overturn rates, underpayment recovery (payer underpayment versus contract terms is a large recoverable pool), and days-to-collection trends.

## Formula

```
NCR-H = Payments Received / Charges Billable at Contracted Rates
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** healthcare_revenue_cycle
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 870 (batch 3)
