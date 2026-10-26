# dea:metric-finding-and-development-cost

Candidate Performance Metric record for **Finding and Development Cost** (FDC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-finding-and-development-cost`
- **Name:** Finding and Development Cost
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FDC

## 2. Definition

Finding and Development Cost (FDC) measures how efficiently resources are converted into outputs in the Oil & Gas domain. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Exploration and Development Cost / Reserves Added, expressed in currency per unit. It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Oil & gas.

## 3. Context

Finding and development cost measures the capital spent per barrel of oil equivalent discovered and developed, and it is the upstream industry's growth-efficiency metric - how much it costs to replace each barrel of production with a new one. The measurement trap is the timing lag: F&D costs divide current-year capital by current-year reserve additions from that capital, but fields take years to develop, so annual figures swing wildly depending on project cadence and reserve revisions (which can book huge volumes with little new spending). The industry solution is multi-year averaging, typically three to five years. Read with reserve replacement ratio (volume view while F&D is cost view), discovery size distribution, and the discovery-versus-acquisition mix for replacing reserves.

## Formula

```
Exploration and Development Cost / Reserves Added
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 882 (batch 3)
