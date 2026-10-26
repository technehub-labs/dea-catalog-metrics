# dea:metric-asset-availability-fleet-critical

Candidate Performance Metric record for **Asset Availability (Fleet Critical)** (AAFC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-asset-availability-fleet-critical`
- **Name:** Asset Availability (Fleet Critical)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** AAFC

## 2. Definition

A Field Service & Asset Performance indicator, Asset Availability (Fleet Critical) (AAFC) quantifies the quality of outputs and outcomes. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Uptime of Critical Assets / Planned Uptime, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of time critical assets are operational and available for service. Availability is the revenue engine of asset-heavy service businesses. Definitions excluding planned maintenance can flatter while hiding capacity erosion. Read with utilization vs. capacity and asset downtime cost per incident.

## Formula

```
AAFC = Uptime of Critical Assets / Planned Uptime
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** operations
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** field_service_asset_performance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3386 (batch 7)
