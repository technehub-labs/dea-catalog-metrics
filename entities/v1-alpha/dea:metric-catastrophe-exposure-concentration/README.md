# dea:metric-catastrophe-exposure-concentration

Candidate Performance Metric record for **Catastrophe Exposure Concentration** (CEC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-catastrophe-exposure-concentration`
- **Name:** Catastrophe Exposure Concentration
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CEC

## 2. Definition

Catastrophe Exposure Concentration (CEC) captures exposure to adverse outcomes for organizations tracking insurance underwriting. It is defined as Catastrophe-Exposed Sum Insured / Total Sum Insured; the result is stated in percent (%). In Insurance, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures accumulation of insured value in catastrophe-prone zones - perils, regions, and total sum at risk. Concentration is the silent balance-sheet killer in insurance: many individually prudent policies form an imprudent portfolio when they share a fault line or coastline. Update exposure inventories continuously, since insured values drift between modeled refreshes. Read with reinsurance treaty limits against modeled event losses and stress test results.

## Formula

```
Catastrophe-Exposed Sum Insured / Total Sum Insured
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_underwriting
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1519 (batch 6)
