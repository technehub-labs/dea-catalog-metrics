# dea:metric-post-clearance-audit-adjustment-rate

Candidate Performance Metric record for **Post-Clearance Audit Adjustment Rate** (PCAAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-post-clearance-audit-adjustment-rate`
- **Name:** Post-Clearance Audit Adjustment Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PCAAR

## 2. Definition

A International Trade & Customs indicator, Post-Clearance Audit Adjustment Rate (PCAAR) quantifies exposure to adverse outcomes. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Audits with Duty Adjustment / Audits, measured in percent (%). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Logistics & Trade practice.

## 3. Context

Measures duty and classification changes arising from customs audits of prior entries. It is the honesty metric of trade compliance: high adjustment rates reveal systematic misclassification or valuation errors, with penalty exposure that scales with found-and-repeated patterns. Segment by broker and lane, since errors cluster where expertise is thin. Read with free trade agreement utilization and broker performance scores.

## Formula

```
PCAAR = Audits with Duty Adjustment / Audits
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** international_trade_customs
- **Sector:** logistics_trade

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1718 (batch 6)
