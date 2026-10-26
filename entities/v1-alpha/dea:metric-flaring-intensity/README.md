# dea:metric-flaring-intensity

Candidate Performance Metric record for **Flaring Intensity** (FLRI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-flaring-intensity`
- **Name:** Flaring Intensity
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FLRI

## 2. Definition

Flaring Intensity (FLRI) measures environmental and social sustainability performance in the Oil & Gas domain. It is computed as Volume Flared / Volume Produced, expressed in percent (%). Its use is concentrated in Oil & gas. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Flaring intensity measures gas burned off at the wellhead per unit of oil produced, and it is the metric where the industry's wastefulness is most publicly visible - flaring is simultaneously a waste of saleable gas, a CO2 and methane emissions source, and a regulatory target (World Bank zero routine flaring initiative) with investor pressure behind it. Flaring happens when gas infrastructure lags oil production: it is fundamentally an infrastructure-timing problem, so intensity falls with gathering pipeline buildout or production curtailment where takeaway is absent. Satellite monitoring (like the World Bank's flare estimates) has made flaring independently observable, removing the self-reporting cover. Read with flaring volume by basin, gas-to-oil ratio of production, takeaway capacity utilization, and methane intensity.

## Formula

```
FLRI = Volume Flared / Volume Produced
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** sustainability
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** oil_gas
- **Sector:** oil_gas

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 885 (batch 3)
