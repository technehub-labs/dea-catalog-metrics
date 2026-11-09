# dea:metric-risk-network-density-index

Candidate Performance Metric record for **Risk Network Density Index** (RNDI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-risk-network-density-index`
- **Name:** Risk Network Density Index
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RNDI

## 2. Definition

A Emerging Risk & Horizon Scanning indicator, Risk Network Density Index (RNDI) quantifies exposure to adverse outcomes. The formula is Connectedness of Risk Clusters in Taxonomy Network - reported in index (0-100 or normalized). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how interconnected the risk landscape is (risk-to-risk dependencies). Density predicts cascade velocity: dense networks propagate shocks faster. Network maps built once decay with the organization. Read with cross-risk correlation mapping coverage and portfolio risk concentration index.

## Formula

```
RNDI = Connectedness of Risk Clusters in Taxonomy Network
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** emerging_risk_horizon_scanning

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4010 (batch 8)
