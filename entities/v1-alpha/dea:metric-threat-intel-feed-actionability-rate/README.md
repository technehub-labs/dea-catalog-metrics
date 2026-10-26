# dea:metric-threat-intel-feed-actionability-rate

Candidate Performance Metric record for **Threat Intel Feed Actionability Rate** (TIFAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-threat-intel-feed-actionability-rate`
- **Name:** Threat Intel Feed Actionability Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TIFAR

## 2. Definition

A Threat Intelligence & Red Team indicator, Threat Intel Feed Actionability Rate (TIFAR) quantifies the economic value created or preserved. It is computed as Intel Items Triggering Defensive Action / Items Consumed, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Intel Items Triggering Defensive Action / Items Consumed
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** threat_intelligence_red_team

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3282 (batch 7)
