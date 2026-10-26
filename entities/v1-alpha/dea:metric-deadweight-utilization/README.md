# dea:metric-deadweight-utilization

Candidate Performance Metric record for **Deadweight Utilization** (DWU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-deadweight-utilization`
- **Name:** Deadweight Utilization
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DWU

## 2. Definition

Deadweight Utilization (DWU) captures the utilization or availability of capacity for organizations tracking maritime & shipping. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Cargo Deadweight Carried / Vessel Deadweight Capacity, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Maritime & shipping.

## 3. Context

Deadweight utilization measures the share of vessel cargo capacity actually used, and it is the load-factor metric of shipping - the marginal cost of carrying cargo on an already-sailing vessel is tiny, so utilization is almost pure margin. The strategic subtlety is overcapacity cycles: fleet capacity grows in discrete chunks (new vessel deliveries) while demand grows smoothly, so utilization swings through multi-year cycles that determine freight rates across the industry. Route and vessel-size mix matter: post-Panamax economics on major trades differ from feeder routes. Read with utilization by trade lane, ballast-leg share (repositioning empty is wasted capacity), freight rate correlation, and slow-steaming behavior (speed reduction is the utilization-shock absorber).

## Formula

```
DWU = Cargo Deadweight Carried / Vessel Deadweight Capacity
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** maritime_shipping
- **Sector:** maritime_shipping

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 979 (batch 3)
