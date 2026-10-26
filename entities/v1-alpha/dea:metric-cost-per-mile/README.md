# dea:metric-cost-per-mile

Candidate Performance Metric record for **Cost per Mile** (CPM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-per-mile`
- **Name:** Cost per Mile
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CPM

## 2. Definition

Cost per Mile (CPM) addresses how efficiently resources are converted into outputs and is a fixture of logistics & transportation reporting. The formula is Total Transport Cost / Total Miles - reported in currency per unit. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Lower values are better; each reduction is an improvement. It is a standard measure in the Logistics sector.

## 3. Context

Measures total operating cost divided by miles driven. It matters as the fundamental unit economics measure for fleet operations. Gaming risk includes deferring maintenance to shrink current period costs at future reliability expense. Read with Fleet Downtime Percentage and Fuel Efficiency trends to confirm low per-mile costs are structural, not deferred.

## Formula

```
Total Transport Cost / Total Miles
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** logistics_transportation
- **Sector:** logistics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 197 (batch 1)
