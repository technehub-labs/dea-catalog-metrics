# dea:metric-ioc-enrichment-latency

Candidate Performance Metric record for **IOC Enrichment Latency** (IOEL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ioc-enrichment-latency`
- **Name:** IOC Enrichment Latency
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** IOEL

## 2. Definition

A Threat Intelligence & Red Team indicator, IOC Enrichment Latency (IOEL) quantifies how efficiently resources are converted into outputs. It is defined as Minutes from Indicator Observed to Enriched Alert; the result is stated in minutes. It is applied across virtually every sector. It is a working-level control: thresholds trigger immediate operational response. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Minutes from Indicator Observed to Enriched Alert
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** risk
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** threat_intelligence_red_team

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3288 (batch 7)
