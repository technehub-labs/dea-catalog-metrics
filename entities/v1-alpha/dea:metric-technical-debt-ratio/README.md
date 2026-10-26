# dea:metric-technical-debt-ratio

Candidate Performance Metric record for **Technical Debt Ratio** (TDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-technical-debt-ratio`
- **Name:** Technical Debt Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TDR

## 2. Definition

Within Software Engineering, Technical Debt Ratio (TDR) is used to gauge exposure to adverse outcomes. Its calculation is Remediation Cost / Development Cost to Rebuild, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

The estimated remediation cost of code-level shortcuts against the cost of developing the system - the quantification that made technical debt a management conversation rather than an engineering complaint. The metaphor carries the economics: like financial debt, taking it on buys speed now at compounding interest later, and the ratio expresses how large the outstanding balance is relative to the codebase itself. Strategic use is decision framing - every product roadmap choice is implicitly a decision to service debt or issue more of it, and the ratio makes that trade visible at the portfolio level. Values creeping above a small single-digit percentage signal a system where change cost is rising structurally, and above double digits, the team is mostly paying interest rather than delivering features.

## Formula

```
Remediation Cost / Development Cost to Rebuild
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** software_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 283 (batch 1)
