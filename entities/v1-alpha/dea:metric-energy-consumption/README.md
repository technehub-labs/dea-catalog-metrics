# dea:metric-energy-consumption

Candidate Performance Metric record for **Energy Consumption** (EC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-energy-consumption`
- **Name:** Energy Consumption
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** EC

## 2. Definition

Within Sustainability & ESG, Energy Consumption (EC) is used to gauge environmental and social sustainability performance. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Total Energy Consumed per Period - reported in megawatt-hours (MWh). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Total energy used by the organization, conventionally in megawatt-hours or gigajoules across all purchased and self-generated sources - the physical base of the entire decarbonization stack, since most emissions and most energy cost flow through this one quantity. Its strategic weight is multiplicity of consequence: energy consumption drives cost (a top-five cost line in heavy industry), Scope 1 and 2 emissions (the dominant driver of both), and resilience (energy security became a board topic with recent price and supply shocks), so a single metric carries three conversations. Read it decomposed by source and site: electricity, natural gas, and fuels each have different price, carbon, and substitutability profiles, and the site-level cut is where efficiency projects are actually selected and funded.

## Formula

```
Total Energy Consumed per Period
```

## Unit

- **Unit reference:** `dea:unit-megawatthour`
- **Unit:** megawatthour
- **Unit label (as published):** megawatt-hours (MWh)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 414 (batch 1)
