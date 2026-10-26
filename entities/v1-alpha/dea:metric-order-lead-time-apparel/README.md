# dea:metric-order-lead-time-apparel

Candidate Performance Metric record for **Order Lead Time (Apparel)** (OLT-A) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-order-lead-time-apparel`
- **Name:** Order Lead Time (Apparel)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** OLT-A

## 2. Definition

A Textile & Apparel indicator, Order Lead Time (Apparel) (OLT-A) quantifies how efficiently resources are converted into outputs. The formula is Days from Order Confirmation to Shipment - reported in days. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. It is a standard measure in the Textile & apparel sector.

## 3. Context

Order lead time in apparel measures days from order placement to delivery, and it is the responsiveness metric at the heart of the industry's structural dilemma: traditional offshore production runs 3-6 month lead times that force inventory commitments before demand is known, while nearshoring trades higher unit cost for speed. The industry's foundational math (popularized by studies of Zara's model) is that longer lead times force deeper markdowns as forecast error compounds - so lead time is actually a markdown-risk metric in disguise. Honest measurement runs from order confirmation, not from production start, since fabric wait and trim sourcing hide in the gap. Read with lead time by origin region versus markdown rate and sell-through, forecast accuracy at order commit time, and flexibility premium (cost increase for speed) per style.

## Formula

```
Days from Order Confirmation to Shipment
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** textile_apparel
- **Sector:** textile_apparel

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 922 (batch 3)
