# dea:metric-methane-emissions-intensity

Candidate Performance Metric record for **Methane Emissions Intensity** (MEI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-methane-emissions-intensity`
- **Name:** Methane Emissions Intensity
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MEI

## 2. Definition

Methane Emissions Intensity (MEI) captures environmental and social sustainability performance for organizations tracking oil & gas. The formula is Methane Emitted / Hydrocarbons Produced - reported in ratio (x:1 or x). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. It is a standard measure in the Oil & gas sector.

## 3. Context

Methane emissions intensity measures leaked and vented methane per unit of production, and it is the climate metric where oil and gas faces the most scrutiny - methane's 80-plus times near-term warming potential means small leaks carry large climate weight, and satellites and aerial surveys now detect large emitters independently. The measurement controversy is central to reading the metric honestly: operator-reported intensities (often under 0.2 percent) conflict with top-down atmospheric studies showing much higher loss rates, suggesting systematic underreporting through measurement methods. The cost asymmetry is favorable: much methane abatement pays for itself in captured gas. Read with leak detection and repair program effectiveness, super-emitter event counts, and measurement methodology disclosures.

## Formula

```
MEI = Methane Emitted / Hydrocarbons Produced
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 886 (batch 3)
