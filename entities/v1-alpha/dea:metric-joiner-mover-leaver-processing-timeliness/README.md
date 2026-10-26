# dea:metric-joiner-mover-leaver-processing-timeliness

Candidate Performance Metric record for **Joiner-Mover-Leaver Processing Timeliness** (JMLPT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-joiner-mover-leaver-processing-timeliness`
- **Name:** Joiner-Mover-Leaver Processing Timeliness
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** JMLPT

## 2. Definition

Joiner-Mover-Leaver Processing Timeliness (JMLPT) captures conformance to standards, plans, or obligations for organizations tracking identity & access management operations. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Access Changes Processed within SLA / Changes - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how quickly identity systems reflect personnel changes, especially movers and leavers. Stale entitlements after internal moves are the quietest form of privilege creep in most organizations. Leaver delays of days, not hours, are a standing insider risk. Read with orphaned account rate and access revocation cycle time.

## Formula

```
Access Changes Processed within SLA / Changes
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** identity_access_management_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2821 (batch 7)
