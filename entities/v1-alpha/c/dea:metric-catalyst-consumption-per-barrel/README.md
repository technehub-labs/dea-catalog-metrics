# dea:metric-catalyst-consumption-per-barrel

Candidate Performance Metric record for **Catalyst Consumption per Barrel** (CCPB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-catalyst-consumption-per-barrel`
- **Name:** Catalyst Consumption per Barrel
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CCPB

## 2. Definition

Catalyst Consumption per Barrel (CCPB) captures how efficiently resources are converted into outputs for organizations tracking oil & gas downstream & refining. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Catalyst Cost / Barrels Processed, measured in currency per unit. It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Oil & Gas practice.

## Formula

```
CCPB = Catalyst Cost / Barrels Processed
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** oil_gas_downstream_refining
- **Sector:** oil_gas

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2304 (batch 6)
