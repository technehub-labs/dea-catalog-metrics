# dea:metric-threat-intel-analyst-utilization

Candidate Performance Metric record for **Threat Intel Analyst Utilization** (TIAU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-threat-intel-analyst-utilization`
- **Name:** Threat Intel Analyst Utilization
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TIAU

## 2. Definition

Threat Intel Analyst Utilization (TIAU) captures the utilization or availability of capacity for organizations tracking threat intelligence & red team. It is defined as Analyst Hours on Strategic Intel / Total Analyst Hours; the result is stated in percent (%). It is applied across virtually every sector. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Values outside the intended band, on either side, warrant investigation.

## Formula

```
Analyst Hours on Strategic Intel / Total Analyst Hours
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** threat_intelligence_red_team

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3296 (batch 7)
