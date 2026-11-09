# dea:metric-greenhouse-gas-scope-2-emissions

Candidate Performance Metric record for **Greenhouse Gas Scope 2 Emissions** (GHG2) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-greenhouse-gas-scope-2-emissions`
- **Name:** Greenhouse Gas Scope 2 Emissions
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** GHG2

## 2. Definition

A Sustainability & ESG indicator, Greenhouse Gas Scope 2 Emissions (GHG2) quantifies environmental and social sustainability performance. It is defined as Indirect Emissions from Purchased Energy; the result is stated in tonnes CO2 equivalent (tCO2e). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Indirect emissions from purchased energy - electricity, steam, heating, and cooling consumed by the organization but generated upstream - the tier where location meets supplier. The GHG Protocol gives it a dual-accounting subtlety that matters strategically: the location-based method uses grid-average factors, while the market-based method honors contractual instruments like power purchase agreements and renewable-energy certificates, and the gap between the two is exactly the emissions value of procurement choices. Scope 2 is the tier most tractable for corporate decarbonization - most large organizations cut faster here than in Scope 1 because renewable contracts change the number faster than process redesign can. Read the grid context: the same factory decarbonizes automatically as its grid decarbonizes, so honest target-setting separates organizational effort from grid luck.

## Formula

```
GHG2 = Indirect Emissions from Purchased Energy
```

## Unit

- **Unit reference:** `dea:unit-tonne`
- **Unit:** tonne
- **Unit label (as published):** tonnes CO2 equivalent (tCO2e)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** sustainability
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** sustainability_esg

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 411 (batch 1)
