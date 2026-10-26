# dea:metric-attack-surface-coverage-external-scan

Candidate Performance Metric record for **Attack Surface Coverage - External Scan** (ASCES) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-attack-surface-coverage-external-scan`
- **Name:** Attack Surface Coverage - External Scan
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ASCES

## 2. Definition

Attack Surface Coverage - External Scan (ASCES) addresses exposure to adverse outcomes and is a fixture of vulnerability & exposure management reporting. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as External Assets Covered by Continuous Scan / Discovered, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how completely external attack surface discovery and scanning covers actual internet-exposed assets. Unknown exposures (shadow DNS, forgotten test systems) are where breaches begin. Discovery against stale asset lists finds only what you already knew. Read with scan coverage - asset base and attack surface reduction rate.

## Formula

```
External Assets Covered by Continuous Scan / Discovered
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** vulnerability_exposure_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2809 (batch 7)
