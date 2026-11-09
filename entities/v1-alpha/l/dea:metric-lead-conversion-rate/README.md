# dea:metric-lead-conversion-rate

Candidate Performance Metric record for **Lead Conversion Rate** (LCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-lead-conversion-rate`
- **Name:** Lead Conversion Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** LCR

## 2. Definition

Lead Conversion Rate (LCR) measures how effectively a process or entity achieves its intended outcome in the Sales domain. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Converted Leads / Total Leads, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of leads that become qualified opportunities or customers. It matters because it locates the funnel's biggest leak and guides marketing spend. It can be gamed by cherry-picking easy low-value leads or redefining what counts as a conversion mid-quarter. Read with Cost per Acquisition and Marketing Qualified Lead Volume to confirm conversions are valuable, not just plentiful.

## Formula

```
LCR = Converted Leads / Total Leads
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sales

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 89 (batch 1)
