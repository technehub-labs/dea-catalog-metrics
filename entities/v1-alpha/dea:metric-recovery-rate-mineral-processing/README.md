# dea:metric-recovery-rate-mineral-processing

Candidate Performance Metric record for **Recovery Rate (Mineral Processing)** (RR-MP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-recovery-rate-mineral-processing`
- **Name:** Recovery Rate (Mineral Processing)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RR-MP

## 2. Definition

A Mining & Metals indicator, Recovery Rate (Mineral Processing) (RR-MP) quantifies how efficiently resources are converted into outputs. Its calculation is Recovered Metal / Metal in Feed Ore, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Mining & metals practice.

## 3. Context

Recovery rate measures the share of valuable metal actually extracted by the mill versus what entered in the ore, and a few percentage points swing translate directly into revenue at full throughput. It is where geology meets metallurgy: recovery depends on ore mineralogy, grind size, reagent chemistry and flotation performance, so it drifts as the ore body changes. A recovery drop is often the earliest visible sign of harder ore or a poorly tuned circuit, well before costs show it. Read alongside head grade and concentrate grade, since pushing recovery too hard can sacrifice product purity and incur smelter penalties.

## Formula

```
Recovered Metal / Metal in Feed Ore
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** mining_metals
- **Sector:** mining_metals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 715 (batch 2)
