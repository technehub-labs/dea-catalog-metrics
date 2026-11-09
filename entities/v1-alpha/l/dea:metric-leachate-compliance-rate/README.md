# dea:metric-leachate-compliance-rate

Candidate Performance Metric record for **Leachate Compliance Rate** (LCR-W) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-leachate-compliance-rate`
- **Name:** Leachate Compliance Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** LCR-W

## 2. Definition

A Waste & Environmental Services indicator, Leachate Compliance Rate (LCR-W) quantifies conformance to standards, plans, or obligations. It is computed as Leachate Samples within Discharge Limits / Samples, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Environmental services.

## 3. Context

Leachate compliance measures adherence to discharge permits for the contaminated liquid that percolates through waste, and it is the groundwater-protection metric for landfill operations - leachate breaches contaminate aquifers for decades, with remediation costs that dwarf compliance costs and legal exposure that outlasts the operating company. Compliance rate understates risk unless read with detection-lag awareness: most leachate systems sample monthly or quarterly, so a slow breach can persist between samples. Older sites without engineered liners, and those exceeding design capacity, carry disproportionate risk. Read with sampling exceedance trends by parameter, liner integrity monitoring, leachate head levels on the liner (the direct pressure driver), and collection-system flow rates.

## Formula

```
LCR-W = Leachate Samples within Discharge Limits / Samples
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** compliance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 821 (batch 2)
