# dea:metric-lifting-cost-per-barrel

Candidate Performance Metric record for **Lifting Cost per Barrel** (LCB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-lifting-cost-per-barrel`
- **Name:** Lifting Cost per Barrel
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LCB

## 2. Definition

Lifting Cost per Barrel (LCB) measures how efficiently resources are converted into outputs in the Oil & Gas domain. The formula is Production Lifting Cost / Barrels Produced - reported in currency per unit. It is a standard measure in the Oil & gas sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Lifting cost per barrel is the operating expense of producing oil from wells already drilled - labor, energy, maintenance, and workovers divided by production - and it is the cash-margin metric of upstream operations. Its dynamic behavior is the key signal: lifting costs rise mechanically as fields age (more water, less oil, more artificial lift), so a rising lifting cost can reflect mature-field economics rather than operational slippage. Offshore lifting costs run multiples of onshore, and artificial lift energy costs dominate in late-life wells. Read with water cut trend (the mechanical driver), workover frequency, and lifting cost relative to netback to gauge how close marginal fields sit to shut-in economics.

## Formula

```
Production Lifting Cost / Barrels Produced
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 881 (batch 3)
