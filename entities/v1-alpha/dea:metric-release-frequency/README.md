# dea:metric-release-frequency

Candidate Performance Metric record for **Release Frequency** (RLF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-release-frequency`
- **Name:** Release Frequency
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RLF

## 2. Definition

Release Frequency (RLF) captures the utilization or availability of capacity for organizations tracking software engineering. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Releases per Period - reported in times per period. Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

How often code changes are deployed to production - the throughput metric of software delivery, and the one that separates deployment as an event from deployment as routine. Its strategic weight comes from what frequency enables: small batches, lower risk per release, faster feedback from users, and the shortening of the idea-to-value loop that the DORA research program found distinguishes high-performing organizations - along with the cultural point that frequent deployment makes deployment boring, and boring is what reliability looks like. The failure mode is measuring frequency alone: deploying daily with high failure rates is worse than deploying weekly with low ones, so this metric is always read with change failure rate and time to restore, exactly as the DORA framework prescribes.

## Formula

```
Releases per Period
```

## Unit

- **Unit reference:** `dea:unit-times`
- **Unit:** times
- **Unit label (as published):** times per period

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** software_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 292 (batch 1)
