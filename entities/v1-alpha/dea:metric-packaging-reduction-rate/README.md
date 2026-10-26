# dea:metric-packaging-reduction-rate

Candidate Performance Metric record for **Packaging Reduction Rate** (PKR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-packaging-reduction-rate`
- **Name:** Packaging Reduction Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PKR

## 2. Definition

Packaging Reduction Rate (PKR) captures environmental and social sustainability performance for organizations tracking sustainability & esg. It is computed as (Packaging_prior - Packaging_current) / Packaging_prior, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the percentage reduction in packaging material per unit or overall. It matters because packaging is highly visible to consumers and regulators and often pure cost. It can be gamed by shifting protective requirements to suppliers or shrinking pack counts while material weight holds. Read with Product Damage Rate in transit and Waste Diversion Rate to confirm lighter packaging does not raise damage losses.

## Formula

```
(Packaging_prior - Packaging_current) / Packaging_prior
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** sustainability
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** sustainability_esg

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 430 (batch 1)
