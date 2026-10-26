# dea:metric-stevedore-injury-rate

Candidate Performance Metric record for **Stevedore Injury Rate** (SIR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-stevedore-injury-rate`
- **Name:** Stevedore Injury Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SIR

## 2. Definition

A Maritime & Shipping indicator, Stevedore Injury Rate (SIR) quantifies exposure to adverse outcomes. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Recordable Injuries / Hours Worked x 200,000, expressed in ratio (x:1 or x). It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Maritime & shipping.

## 3. Context

Stevedore injury rate measures injuries per hours worked on the dock, and it is the safety metric of one of the most dangerous occupations in transportation - cargo handling combines heavy loads, working at height on lashed containers, vehicle movement in tight spaces, and suspended-load exposure. The industry's safety transformation is documented but uneven: mechanization and vessel design improvements cut rates over decades, but container-lashing work at height remains a stubborn exposure. The underreporting risk is elevated in casualized labor arrangements, so rates should be validated against insurance claims data. Read with injury severity distribution (fatal and major-injury counts matter more than first-aid frequency), lost-time injury trend, high-risk task exposure hours, and near-miss reporting rates as leading indicators.

## Formula

```
Recordable Injuries / Hours Worked x 200,000
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** maritime_shipping
- **Sector:** maritime_shipping

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 989 (batch 3)
