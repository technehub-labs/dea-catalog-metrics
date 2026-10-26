# dea:metric-port-state-control-detention-rate

Candidate Performance Metric record for **Port State Control Detention Rate** (PSCD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-port-state-control-detention-rate`
- **Name:** Port State Control Detention Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PSCD

## 2. Definition

Port State Control Detention Rate (PSCD) addresses conformance to standards, plans, or obligations and is a fixture of maritime & shipping reporting. Its calculation is Inspections Ending in Detention / Inspections, measured in percent (%). It originates from and is most used in Maritime & shipping practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Port State Control detention rate measures the share of vessel inspections resulting in detention - the metric that governs a ship's global operating freedom, since detention means a vessel cannot sail until deficiencies are cleared, at direct cost and reputational damage to its registry and operator. PSC regimes (Paris and Tokyo MOUs being the largest) target-inspect based on risk profiles, so detention rates reflect both ship quality and inspection-selection bias. The metric's real power is systemic: flag states and classification societies are ranked publicly, and high-detention flags lose business, making the metric an industry-quality enforcement mechanism. Read with deficiency items by category (ISM code items indicate management failures rather than hardware), inspection history (repeat-deficiency vessels concentrate risk), and flag-state performance lists.

## Formula

```
Inspections Ending in Detention / Inspections
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 984 (batch 3)
