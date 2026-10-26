# dea:metric-desk-sharing-ratio

Candidate Performance Metric record for **Desk Sharing Ratio** (DSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-desk-sharing-ratio`
- **Name:** Desk Sharing Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DSR

## 2. Definition

Desk Sharing Ratio (DSR) measures the utilization or availability of capacity in the Facilities & Real Estate domain. It is defined as Employees / Workstations; the result is stated in ratio (x:1 or x). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. Values outside the intended band, on either side, warrant investigation.

## 3. Context

The ratio of employees to desks in a workplace - the design parameter that hybrid work made measurable, since sharing ratios near one assumed attendance near one, and hybrid attendance broke that assumption permanently. Its strategic significance is the arbitrage it quantifies: attendance below full capacity means desks sit unused, and raising the ratio converts that slack into reduced leased area - but only up to the experience boundary, where sharing ratios high enough to create desk scarcity on peak days push employees to stay home rather than compete for space, undoing the attendance the office strategy was built to recover. The honest measurement is peak-day, not average: a ratio comfortable on average that fails on Tuesdays is a failed design, which is why utilization data by weekday is the required input before choosing the ratio.

## Formula

```
Employees / Workstations
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** facilities_real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 459 (batch 1)
