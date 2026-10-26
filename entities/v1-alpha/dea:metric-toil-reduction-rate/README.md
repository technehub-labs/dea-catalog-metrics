# dea:metric-toil-reduction-rate

Candidate Performance Metric record for **Toil Reduction Rate** (TRR-SRE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-toil-reduction-rate`
- **Name:** Toil Reduction Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** TRR-SRE

## 2. Definition

Toil Reduction Rate (TRR-SRE) captures how efficiently resources are converted into outputs for organizations tracking observability & site reliability engineering. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Reduction in Manual Operational Work Hours per Quarter - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the pace at which manual, repetitive, automatable operational work is eliminated. Toil is a tax on engineering capacity that compounds silently. Automation projects often create new toil (maintaining the automation) while retiring old. Read with toil-to-work ratio and auto-remediation execution rate.

## Formula

```
Reduction in Manual Operational Work Hours per Quarter
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** observability_site_reliability_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2875 (batch 7)
