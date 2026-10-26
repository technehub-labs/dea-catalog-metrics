# dea:metric-payment-processing-uptime

Candidate Performance Metric record for **Payment Processing Uptime** (PPU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-payment-processing-uptime`
- **Name:** Payment Processing Uptime
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PPU

## 2. Definition

Payment Processing Uptime (PPU) captures the quality of outputs and outcomes for organizations tracking payments & fintech. The formula is Available Processing Time / Total Time - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Payments & fintech sector.

## 3. Context

Payment processing uptime measures the availability of the transaction authorization infrastructure, and it is unusual among uptime metrics in that its downtime cost is instantaneous and public - a 30-minute outage means every attempted purchase fails in real time at the shelf, with abandonment rather than retry. Enterprise payments platforms contract to 99.99 percent or better, but the honest metric is effective authorization success rate, which blends uptime, latency, and issuer availability, since a slow-but-up system still loses transactions. Distributed architectures trade uptime against consistency, and the maintenance-window question matters for global merchants. Read with authorization rate excluding outage windows, mean time to recovery, and revenue-per-minute-of-outage for the business translation.

## Formula

```
Available Processing Time / Total Time
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** payments_fintech
- **Sector:** payments_fintech

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 778 (batch 2)
