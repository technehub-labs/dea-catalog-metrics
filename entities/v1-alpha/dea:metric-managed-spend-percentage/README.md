# dea:metric-managed-spend-percentage

Candidate Performance Metric record for **Managed Spend Percentage** (MSP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-managed-spend-percentage`
- **Name:** Managed Spend Percentage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MSP

## 2. Definition

Within Procurement, Managed Spend Percentage (MSP) is used to gauge how effectively a process or entity achieves its intended outcome. Its calculation is Spend via Managed Contracts / Total Spend, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The proportion of addressable spend governed by procurement agreements and channels - the operational refinement of spend under management that asks not whether procurement was involved once, but whether the buying actually flows through negotiated terms. The gap between the two metrics is compliance leakage: spend that was sourced under a contract but bought off-contract through unguided purchasing or tail suppliers, which is where negotiated savings quietly evaporate. Strategic use is as the compliance engine of the savings story, since savings that are negotiated but not enforced are a projection, not a result. The remediation levers are known - catalog coverage, approval thresholds, payment-method control - which makes this one of the few metrics where the improvement playbook is genuinely standard.

## Formula

```
Spend via Managed Contracts / Total Spend
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** procurement

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 224 (batch 1)
