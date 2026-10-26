# dea:metric-sulfur-recovery-efficiency

Candidate Performance Metric record for **Sulfur Recovery Efficiency** (SRE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-sulfur-recovery-efficiency`
- **Name:** Sulfur Recovery Efficiency
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SRE

## 2. Definition

Sulfur Recovery Efficiency (SRE) measures environmental and social sustainability performance in the Oil & Gas Downstream & Refining domain. Its calculation is Sulfur Recovered / Sulfur in Feed, measured in percent (%). It originates from and is most used in Oil & Gas practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures sulfur recovery unit performance against design and permit requirements. It is the emissions-compliance choke point of refining - sulfur limits on fuels and SO2 permits both pass through SRU performance - and recovery shortfalls constrain throughput economics directly. Efficiency must be read against feed sulfur load, since sourer slates stress recovery capacity. Read with emissions compliance trends and fuels-specification upgrade economics.

## Formula

```
SRE = Sulfur Recovered / Sulfur in Feed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** sustainability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** oil_gas_downstream_refining
- **Sector:** oil_gas

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2309 (batch 6)
