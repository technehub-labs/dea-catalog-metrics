# dea:metric-vessel-schedule-reliability

Candidate Performance Metric record for **Vessel Schedule Reliability** (VSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-vessel-schedule-reliability`
- **Name:** Vessel Schedule Reliability
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** VSR

## 2. Definition

Within Maritime & Shipping, Vessel Schedule Reliability (VSR) is used to gauge the quality of outputs and outcomes. The formula is Voyages Arriving within Schedule Tolerance / Voyages - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Maritime & shipping sector.

## 3. Context

Vessel schedule reliability measures the share of vessels arriving within a day of schedule, and it is the container-shipping metric that defines the industry's service quality - after 2021's supply-chain crisis, when reliability collapsed below 40 percent on major trades, it became the metric that justified enormous freight-rate premiums for carriers who could still run to schedule. The metric's economic logic is that shippers' supply chains depend on vessel arrival times: a missed vessel connection can idle a factory, so reliability is priced. It is also a capacity-management signal: reliability collapses when demand exceeds capacity (congestion cascades through ports) and recovers when slack returns. Read with reliability by trade lane and carrier, port congestion indices, blank-sailing frequency, and average delay magnitude rather than just binary on-time counts.

## Formula

```
VSR = Voyages Arriving within Schedule Tolerance / Voyages
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** maritime_shipping
- **Sector:** maritime_shipping

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 978 (batch 3)
