# dea:metric-sustainment-rate-of-improvements

Candidate Performance Metric record for **Sustainment Rate of Improvements** (SRI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-sustainment-rate-of-improvements`
- **Name:** Sustainment Rate of Improvements
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SRI

## 2. Definition

A Process Excellence (Lean Six Sigma) indicator, Sustainment Rate of Improvements (SRI) quantifies the quality of outputs and outcomes. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Improvements Sustaining Gains after 6 Months / Improvements Closed, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Sustainment rate of improvements measures the share of implemented process changes that persist over time - still being followed, still producing benefit months or quarters later - and it is the metric that catches the improvement program's dirty secret: a large share of improvements decay back, as old habits, staffing pressure, and competing priorities erode new standards. Sustainability is where improvement differs from theater: a program that generates 100 improvements with 30 percent sustainment creates less value than one generating 30 with 90 percent sustainment, and the second organization is building real capability. The sustainment levers are known: standard-work documentation, layered process audits, visual management, and leadership standard work that keeps attention on the new process. Read with audit-finding decay curves (repeat findings from process audits reveal erosion), benefit-tracking persistence, and layer-audit completion rate.

## Formula

```
Improvements Sustaining Gains after 6 Months / Improvements Closed
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** capability
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** process_excellence_lean_six_sigma

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1123 (batch 4)
