# dea:metric-adjuster-case-load-deep-dive

Candidate Performance Metric record for **Adjuster Case Load (Deep Dive)** (ACL-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-adjuster-case-load-deep-dive`
- **Name:** Adjuster Case Load (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ACL-D

## 2. Definition

Within Insurance Claims Deep Dive, Adjuster Case Load (Deep Dive) (ACL-D) is used to gauge the utilization or availability of capacity. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Open Claims per Adjuster - reported in count (items per period). The objective is neither maximization nor minimization but staying within an agreed operating band. It is a standard measure in the Insurance sector.

## Formula

```
ACL-D = Open Claims per Adjuster
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** financial
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_claims_deep_dive
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1558 (batch 6)
