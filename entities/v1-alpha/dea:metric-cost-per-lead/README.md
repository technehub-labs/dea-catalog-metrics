# dea:metric-cost-per-lead

Candidate Performance Metric record for **Cost per Lead** (CPL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-per-lead`
- **Name:** Cost per Lead
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CPL

## 2. Definition

Cost per Lead (CPL) captures how efficiently resources are converted into outputs for organizations tracking marketing. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Total Campaign Cost / Leads Generated, expressed in currency per unit. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures average marketing spend to generate one lead. It matters because it sets the economics of the funnel and flags channel inefficiency. Gaming risk includes shifting spend to cheap low-intent channels or crediting organic leads to paid campaigns. Read with MQL to SQL Conversion and Cost per Acquisition to ensure cheaper leads are not simply worse leads.

## Formula

```
Total Campaign Cost / Leads Generated
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** marketing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 109 (batch 1)
