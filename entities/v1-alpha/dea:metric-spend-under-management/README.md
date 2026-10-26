# dea:metric-spend-under-management

Candidate Performance Metric record for **Spend under Management** (SuM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-spend-under-management`
- **Name:** Spend under Management
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SuM

## 2. Definition

A Supply Chain indicator, Spend under Management (SuM) quantifies how effectively a process or entity achieves its intended outcome. Its calculation is Managed Spend / Total Addressable Spend, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

The share of total third-party spend that flows through the procurement function with its processes - the foundational coverage metric of the procurement operating model, because a category that procurement never sees is bought without leverage, policy, or data. Levels below 50 percent mean most spend is invisible to the discipline, and every other procurement metric is computed on a fraction of the base. Strategic use is prioritized expansion: bringing the top unmanaged categories under management is usually worth more than squeezing the already-managed ones, and the metric measures exactly that frontier. The definitional care is what counts as under management - strategic sourcing engagement versus compliance-enforced buying channels differ materially, so the number should always travel with its definition.

## Formula

```
Managed Spend / Total Addressable Spend
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
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** supply_chain

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 193 (batch 1)
