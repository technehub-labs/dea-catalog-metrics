# dea:metric-straight-through-processing-rate-claims

Candidate Performance Metric record for **Straight-Through Processing Rate (Claims)** (STP-C) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-straight-through-processing-rate-claims`
- **Name:** Straight-Through Processing Rate (Claims)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** STP-C

## 2. Definition

Straight-Through Processing Rate (Claims) (STP-C) measures how efficiently resources are converted into outputs in the Claims Operations (Insurance) domain. The formula is Claims Settled without Manual Intervention / Claims Received - reported in percent (%). It is a standard measure in the Insurance sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Straight-through processing rate measures the share of claims settled without human touch, and it is the efficiency frontier of claims operations - simple claims (glass repair, small property losses) can flow through rules-based adjudication in minutes, cutting loss-adjustment expense and cycle time simultaneously. The strategic subtlety is threshold calibration: pushing more claims into STP raises efficiency but risks under-investigating borderline claims (a leakage-versus-expense trade-off in reverse), and fraud rings specifically probe STP thresholds with just-below-limit claims. STP rate by claim type matters more than blended rate. Read with STP claim accuracy audits, average STP claim size versus manual threshold, cycle-time comparison STP versus touched claims, and fraud hit rates on STP-routed claims.

## Formula

```
Claims Settled without Manual Intervention / Claims Received
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** claims_operations_insurance
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 848 (batch 3)
