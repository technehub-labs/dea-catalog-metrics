# dea:metric-underwriter-workload-utilization

Candidate Performance Metric record for **Underwriter Workload Utilization** (UWU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-underwriter-workload-utilization`
- **Name:** Underwriter Workload Utilization
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** UWU

## 2. Definition

Underwriter Workload Utilization (UWU) captures the utilization or availability of capacity for organizations tracking insurance underwriting. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Active Underwriting Hours / Available Hours, expressed in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Its use is concentrated in Insurance.

## Formula

```
Active Underwriting Hours / Available Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_underwriting
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1510 (batch 6)
