# dea:metric-inbound-license-compliance-rate

Candidate Performance Metric record for **Inbound License Compliance Rate** (ILCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-inbound-license-compliance-rate`
- **Name:** Inbound License Compliance Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ILCR

## 2. Definition

Inbound License Compliance Rate (ILCR) captures exposure to adverse outcomes for organizations tracking intellectual property & licensing. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Third-Party IP Usage within License Terms / Usage Sampled - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
ILCR = Third-Party IP Usage within License Terms / Usage Sampled
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** intellectual_property_licensing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3944 (batch 8)
