# dea:metric-technical-performance-measure-variance

Candidate Performance Metric record for **Technical Performance Measure Variance** (TPMV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-technical-performance-measure-variance`
- **Name:** Technical Performance Measure Variance
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TPMV

## 2. Definition

Technical Performance Measure Variance (TPMV) addresses the quality of outputs and outcomes and is a fixture of aerospace & defense program management reporting. It is computed as Actual TPM - Threshold TPM / Threshold, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is concentrated in Aerospace & Defense.

## 3. Context

Measures deviation of actual technical parameters - weight, range, power, signature - against committed thresholds. In complex programs, technical variance is the root of schedule and cost trouble long before money shows it, since every capability shortfall eventually becomes redesign. Track margin management against thresholds, not just point variance. Read with design review closure and mass properties trends.

## Formula

```
Actual TPM - Threshold TPM / Threshold
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** aerospace_defense_program_management
- **Sector:** aerospace_defense

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1779 (batch 6)
