# dea:metric-commission-to-premium-ratio

Candidate Performance Metric record for **Commission-to-Premium Ratio** (CPR-I) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-commission-to-premium-ratio`
- **Name:** Commission-to-Premium Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CPR-I

## 2. Definition

Within Insurance Distribution & Agency Management, Commission-to-Premium Ratio (CPR-I) is used to gauge how efficiently resources are converted into outputs. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Commissions Paid / Written Premium, expressed in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Its use is concentrated in Insurance.

## 3. Context

Measures distribution cost as a share of written premium. It is the core economics dial of agency management, balancing motivation against margin, and rising ratios in flat markets signal incentive structure drift. Beware ratio games with renewal commissions counted against new premium, and mix effects when product mix shifts. Read with agency persistency rate for whether the spend buys durable business.

## Formula

```
CPR-I = Commissions Paid / Written Premium
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** insurance_distribution_agency_management
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1726 (batch 6)
