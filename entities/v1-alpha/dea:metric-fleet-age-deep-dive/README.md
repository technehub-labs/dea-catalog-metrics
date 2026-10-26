# dea:metric-fleet-age-deep-dive

Candidate Performance Metric record for **Fleet Age (Deep Dive)** (FA-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fleet-age-deep-dive`
- **Name:** Fleet Age (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FA-D

## 2. Definition

Fleet Age (Deep Dive) (FA-D) measures capability maturity or development in the Airline Operations (Deep Dive) domain. It is computed as Average Years Since Manufacture, expressed in years. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is concentrated in Airlines.

## 3. Context

Measures the average age of the operating fleet. Fleet age is the strategic-ambiguity metric of airlines: younger fleets cut fuel and maintenance cost and support brand and emissions positioning, but fleet renewal is capital-intensive and cycles poorly timed destroy balance sheets. Age must be read with type-specific economics and lease-end walls, since averages hide renewal cliffs. Read with technical dispatch reliability (Deep Dive) and capital expenditure phasing.

## Formula

```
Average Years Since Manufacture
```

## Unit

- **Unit reference:** `dea:unit-year`
- **Unit:** year
- **Unit label (as published):** years

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airline_operations_deep_dive
- **Sector:** airlines

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2265 (batch 6)
