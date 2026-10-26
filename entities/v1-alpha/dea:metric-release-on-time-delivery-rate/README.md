# dea:metric-release-on-time-delivery-rate

Candidate Performance Metric record for **Release On-Time Delivery Rate** (ROTD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-release-on-time-delivery-rate`
- **Name:** Release On-Time Delivery Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ROTD

## 2. Definition

Release On-Time Delivery Rate (ROTD) captures conformance to standards, plans, or obligations for organizations tracking release management & environments. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Releases Delivered on Committed Date / Releases, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of releases delivered within their committed window. Predictability matters more than raw speed for planning-dependent business partners and customers. A high rate can reflect sandbagged commitments or scope-cutting rather than genuine capability. Read with release cycle time and estimate accuracy - schedule.

## Formula

```
Releases Delivered on Committed Date / Releases
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** release_management_environments

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2730 (batch 7)
