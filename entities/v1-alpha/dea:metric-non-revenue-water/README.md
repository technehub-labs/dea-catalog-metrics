# dea:metric-non-revenue-water

Candidate Performance Metric record for **Non-Revenue Water** (NRW) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-non-revenue-water`
- **Name:** Non-Revenue Water
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** NRW

## 2. Definition

Non-Revenue Water (NRW) measures how efficiently resources are converted into outputs in the Energy & Utilities domain. The formula is Water Lost / Water Supplied - reported in percent (%). It is a standard measure in the Energy & utilities sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Water produced but not billed - the share of treated, pumped water lost to leaks, metering inaccuracy, or unauthorized consumption before it reaches paying customers. Its strategic significance is the brutal economics of water infrastructure: every lost cubic meter carries full treatment and pumping cost with zero recovery, and systems losing large fractions of their output (some utilities lose half) are financing a hidden second network. The decomposition is the diagnostic: real losses (leaks) are a capital-integrity question answered by pressure management and mains renewal, while apparent losses (metering and theft) are a revenue-integrity question answered by metering programs - and the two demand opposite investments, so NRW programs always start with the water-balance audit that splits them. Regulators increasingly set loss targets, which converts this from an engineering statistic into a compliance metric with rate-case consequence.

## Formula

```
Water Lost / Water Supplied
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** energy_utilities
- **Sector:** energy_utilities

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 443 (batch 1)
