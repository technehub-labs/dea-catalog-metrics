# dea:metric-customer-returns-rate

Candidate Performance Metric record for **Customer Returns Rate** (CRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-customer-returns-rate`
- **Name:** Customer Returns Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CRR

## 2. Definition

Customer Returns Rate (CRR) addresses the quality of outputs and outcomes and is a fixture of quality management reporting. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Returned Units / Units Sold - reported in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Units returned by customers as a share of units sold - the quality signal that arrives from the only judge whose opinion matters. Its strategic weight is the diagnostic map it provides: returns clustered by reason code separate product defects (manufacturing problem), sizing or description mismatches (content problem), buyer-remorse patterns (marketing and assortment problem), and damage in transit (packaging and logistics problem) - the same headline rate with entirely different remedies. The financial exposure exceeds the refund value, since reverse logistics, refurbishment, and write-offs roughly double the direct cost. E-commerce runs structurally higher than physical retail because buying without touching shifts the risk of mismatch onto the seller, which is why the honest comparison matches channels, not just companies.

## Formula

```
Returned Units / Units Sold
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** capability
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** quality_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 236 (batch 1)
