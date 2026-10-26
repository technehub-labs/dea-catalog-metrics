# dea:metric-operational-disruption-loss-value

Candidate Performance Metric record for **Operational Disruption Loss Value** (ODLV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-operational-disruption-loss-value`
- **Name:** Operational Disruption Loss Value
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ODLV

## 2. Definition

Operational Disruption Loss Value (ODLV) measures exposure to adverse outcomes in the Business Resilience & Continuity domain. The formula is Financial Impact of Disruptions per Period - reported in currency value. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the financial impact of operational disruptions - lost revenue, remediation cost, penalties, customer compensation - over a period. It converts resilience from technical compliance into CFO language and enables return-on-resilience investment analysis. Attribution matters: including everything overstates resilience ROI, while excluding customer-lifetime-value damage understates it. Read with single point of failure count and disruption frequency by cause.

## Formula

```
Financial Impact of Disruptions per Period
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** business_resilience_continuity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1419 (batch 5)
