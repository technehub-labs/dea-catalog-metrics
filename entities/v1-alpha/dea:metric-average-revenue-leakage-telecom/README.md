# dea:metric-average-revenue-leakage-telecom

Candidate Performance Metric record for **Average Revenue Leakage (Telecom)** (ARLT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-revenue-leakage-telecom`
- **Name:** Average Revenue Leakage (Telecom)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ARLT

## 2. Definition

A Telecom Customer Experience & Billing indicator, Average Revenue Leakage (Telecom) (ARLT) quantifies the economic value created or preserved. The formula is Billed Value Shortfalls / Total Billed Value - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. It is a standard measure in the Telecommunications sector.

## 3. Context

Quantifies revenue lost to unbilled services, mis-rated usage, provisioning mismatches, and credit not applied - money earned operationally but never collected. In telecom, leakage commonly runs one to three percent of revenue, a material drag that never appears as a cost line. Be honest about estimation methodology: audit-sample leakage extrapolated to the base overstates the recoverable portion, and some leakage is deliberately tolerated as goodwill. Read with billing accuracy rate (Telecom) and order-to-bill reconciliation coverage.

## Formula

```
Billed Value Shortfalls / Total Billed Value
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** telecom_customer_experience_billing
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1269 (batch 5)
