# dea:metric-threat-intelligence-integration-coverage

Candidate Performance Metric record for **Threat Intelligence Integration Coverage** (TIIC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-threat-intelligence-integration-coverage`
- **Name:** Threat Intelligence Integration Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TIIC

## 2. Definition

Threat Intelligence Integration Coverage (TIIC) addresses capability maturity or development and is a fixture of secops & security operations center reporting. The formula is Detection Sources Enriched with TI / Detection Sources - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of detection and prevention tooling consuming relevant threat intelligence feeds. Intel turns generic monitoring into anticipatory defense tuned to your actual adversaries. Stock feeds without curation create alert noise that degrades SOC response. Read with detection rule coverage against MITRE ATT&CK and MTTD - security.

## Formula

```
TIIC = Detection Sources Enriched with TI / Detection Sources
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** secops_security_operations_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2780 (batch 7)
