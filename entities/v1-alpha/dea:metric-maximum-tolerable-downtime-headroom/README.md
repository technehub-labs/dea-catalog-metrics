# dea:metric-maximum-tolerable-downtime-headroom

Candidate Performance Metric record for **Maximum Tolerable Downtime Headroom** (MTDH) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-maximum-tolerable-downtime-headroom`
- **Name:** Maximum Tolerable Downtime Headroom
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MTDH

## 2. Definition

Maximum Tolerable Downtime Headroom (MTDH) addresses exposure to adverse outcomes and is a fixture of business continuity & disaster recovery reporting. It is defined as Demonstrated Recovery Time vs Maximum Tolerable Downtime; the result is stated in ratio (x:1 or x). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures the buffer between recoverable downtime capability and the maximum the business can absorb. Headroom is what converts an incident from survivable to existential. Headroom computed against untested recovery times is theoretical. Read with recovery time objective compliance rate and business downtime per crisis event.

## Formula

```
Demonstrated Recovery Time vs Maximum Tolerable Downtime
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** business_continuity_disaster_recovery

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3529 (batch 8)
