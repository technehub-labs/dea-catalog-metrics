# dea:metric-design-reuse-rate

Candidate Performance Metric record for **Design Reuse Rate** (DRR-E) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-design-reuse-rate`
- **Name:** Design Reuse Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DRR-E

## 2. Definition

Within Engineering & Design, Design Reuse Rate (DRR-E) is used to gauge how efficiently resources are converted into outputs. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Reused Components or Modules / Total Components, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of new designs composed of previously validated modules, platforms, or subsystems. Reuse is the compounding engine of engineering productivity: it cuts design time, certifies once and uses many times, and concentrates quality improvements across programs. Counted honestly, reuse must exclude copies that require rework, and gauge costs must be reconciled with the benefits log. Read with standard parts utilization and design-to-cost attainment.

## Formula

```
Reused Components or Modules / Total Components
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** engineering_design

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1763 (batch 6)
