# dea:metric-asset-downtime-cost-per-incident

Candidate Performance Metric record for **Asset Downtime Cost per Incident** (ADCI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-asset-downtime-cost-per-incident`
- **Name:** Asset Downtime Cost per Incident
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ADCI

## 2. Definition

Asset Downtime Cost per Incident (ADCI) measures exposure to adverse outcomes in the Field Service & Asset Performance domain. The formula is Total Downtime Cost / Downtime Incidents - reported in currency per unit. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the average financial impact of asset downtime events. It converts reliability into the language of the P&L. Cost models that undercount labor and customer penalties understate urgency. Read with asset availability (Fleet Critical) and mean time between failures (Critical Assets).

## Formula

```
Total Downtime Cost / Downtime Incidents
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** operations
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** field_service_asset_performance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3385 (batch 7)
