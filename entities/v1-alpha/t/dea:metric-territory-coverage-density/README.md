# dea:metric-territory-coverage-density

Candidate Performance Metric record for **Territory Coverage Density** (TCD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-territory-coverage-density`
- **Name:** Territory Coverage Density
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TCD

## 2. Definition

Territory Coverage Density (TCD) measures the utilization or availability of capacity in the Insurance Distribution & Agency Management domain. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Active Appointed Producers / Designated Territory, expressed in count (items per period). The objective is neither maximization nor minimization but staying within an agreed operating band. Its use is concentrated in Insurance.

## 3. Context

Measures distribution presence - agencies or producers per market or per capita of insurable demand. Coverage gaps cap growth regardless of producer productivity, since insurance remains a local, relationship-driven sale in most lines. Density must be read with territory economics: coverage that does not pay for itself is expansion theater. Read with agency plan growth attainment and quotes per territory.

## Formula

```
TCD = Active Appointed Producers / Designated Territory
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** customer
- **Purpose classification:** capacity
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1735 (batch 6)
