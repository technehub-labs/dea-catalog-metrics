# dea:metric-technical-debt-ratio-deep-dive

Candidate Performance Metric record for **Technical Debt Ratio (Deep Dive)** (TDR-SA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-technical-debt-ratio-deep-dive`
- **Name:** Technical Debt Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TDR-SA

## 2. Definition

Technical Debt Ratio (Deep Dive) (TDR-SA) captures exposure to adverse outcomes for organizations tracking software architecture & technical design. It is computed as Remediation Cost / Development Cost, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures remediation cost of technical debt against development cost - the industry-standard normalizing yardstick. It converts an abstract engineering complaint into an economic number leadership can prioritize against, and its trajectory shows whether debt is being managed or accumulated. Measurement honesty depends on the debt inventory being real (scanner plus architectural assessment), since invisible debt is still debt. Read with change failure rate and development velocity trends for the felt cost.

## Formula

```
Remediation Cost / Development Cost
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
- **Domain:** software_architecture_technical_design

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2623 (batch 7)
