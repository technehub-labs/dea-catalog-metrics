# dea:metric-demurrage-and-detention-cost-ratio

Candidate Performance Metric record for **Demurrage and Detention Cost Ratio** (DDCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-demurrage-and-detention-cost-ratio`
- **Name:** Demurrage and Detention Cost Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DDCR

## 2. Definition

Demurrage and Detention Cost Ratio (DDCR) measures how efficiently resources are converted into outputs in the International Trade & Customs domain. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Demurrage and Detention Charges / Freight Spend - reported in percent (%). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Logistics & Trade sector.

## Formula

```
DDCR = Demurrage and Detention Charges / Freight Spend
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** international_trade_customs
- **Sector:** logistics_trade

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1716 (batch 6)
