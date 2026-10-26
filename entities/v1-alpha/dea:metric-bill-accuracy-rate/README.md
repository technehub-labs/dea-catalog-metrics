# dea:metric-bill-accuracy-rate

Candidate Performance Metric record for **Bill Accuracy Rate** (BAR-U) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-bill-accuracy-rate`
- **Name:** Bill Accuracy Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BAR-U

## 2. Definition

Within Utilities Customer Operations, Bill Accuracy Rate (BAR-U) is used to gauge the quality of outputs and outcomes. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Bills Issued without Correction / Bills Issued, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Utilities.

## 3. Context

Bill accuracy rate measures the share of utility bills issued without errors, and it is the trust-utility metric - incorrect bills are the single most corrosive customer experience in a sector where customers cannot switch providers, making billing errors pure frustration with no exit option. Accuracy problems trace to meter-to-bill data flow: estimated reads (when actual meter reads lag), rate application errors, and system migrations concentrate the errors. The industry's smart meter transition changed the game by making actual-read billing nearly universal and making accuracy a data-integration problem rather than a meter-reading logistics one. Read with estimated-bill share, bill adjustment and rebill frequency, complaint rate attributable to billing, and first-call resolution rate on billing issues.

## Formula

```
Bills Issued without Correction / Bills Issued
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** utilities_customer_operations
- **Sector:** utilities

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 957 (batch 3)
