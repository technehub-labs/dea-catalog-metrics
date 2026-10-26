# dea:metric-landfill-diversion-rate

Candidate Performance Metric record for **Landfill Diversion Rate** (LDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-landfill-diversion-rate`
- **Name:** Landfill Diversion Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** LDR

## 2. Definition

A Waste & Environmental Services indicator, Landfill Diversion Rate (LDR) quantifies environmental and social sustainability performance. The formula is Diverted Waste / Total Waste Collected - reported in percent (%). It is a standard measure in the Environmental services sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Landfill diversion rate measures the share of waste stream tonnage redirected from disposal to recycling, composting, or energy recovery, and it is the headline metric of municipal and corporate waste programs alike, often carrying regulatory targets or extended-producer-responsibility implications. Its gaming vector is destination classification: diversion measured at the curb (what was collected separately) overstates true diversion, because contaminated recyclables get re-routed to landfill downstream - material recovery facility rejection rates are the honest correction. Weight-based measurement also biases toward heavy materials like construction debris over plastic film. Read with MRF residue rates, end-market verification for diverted materials, and contamination rates by stream.

## Formula

```
Diverted Waste / Total Waste Collected
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** sustainability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** waste_environmental_services
- **Sector:** environmental_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 816 (batch 2)
