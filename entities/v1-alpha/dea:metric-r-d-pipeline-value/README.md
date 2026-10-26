# dea:metric-r-d-pipeline-value

Candidate Performance Metric record for **R&D Pipeline Value** (RDPV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-r-d-pipeline-value`
- **Name:** R&D Pipeline Value
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RDPV

## 2. Definition

Within Pharma R&D & Clinical Trials, R&D Pipeline Value (RDPV) is used to gauge the economic value created or preserved. The formula is Risk-Adjusted NPV of Pipeline Candidates - reported in currency value. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Pharmaceuticals sector.

## 3. Context

Measures risk-adjusted value of the development pipeline - typically probability-weighted forecast peak sales or net present value by phase. It is the strategic scoreboard of pharma: the company's future is this number plus negotiation capacity. Risk-adjustment assumptions are the battleground, and over-optimistic probability of success weighting systematically inflates value ahead of late-phase failures. Read with phase transition success rate experience against the probabilities used.

## Formula

```
Risk-Adjusted NPV of Pipeline Candidates
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** pharma_r_d_clinical_trials
- **Sector:** pharmaceuticals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1615 (batch 6)
