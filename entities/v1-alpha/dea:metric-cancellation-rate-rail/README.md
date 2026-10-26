# dea:metric-cancellation-rate-rail

Candidate Performance Metric record for **Cancellation Rate (Rail)** (CNR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cancellation-rate-rail`
- **Name:** Cancellation Rate (Rail)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CNR

## 2. Definition

Cancellation Rate (Rail) (CNR) captures exposure to adverse outcomes for organizations tracking rail transport. It is computed as Cancelled Trains / Scheduled Trains, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is concentrated in Rail.

## 3. Context

Cancellation rate measures the share of scheduled trains not run, and it is the punctuality companion metric that exposes the trade - operators can raise punctuality by cancelling late-running trains (the operational temptation is real, and regulators increasingly measure both to prevent it). Cancellation causes differ in kind: rolling stock failures, staff shortage, and infrastructure faults have different fix profiles, and short-notice cancellations damage passengers far more than advance notice ones. The metric's distribution matters: cancellations concentrating at peak hours or on specific routes signal capacity shortfall rather than reliability problems. Read with cancellation cause distribution, short-notice versus planned cancellation share, passenger-weighted cancellation impact (a cancelled peak train displaces hundreds while an off-peak one displaces dozens), and the punctuality/cancellation pair to detect the gaming trade-off.

## Formula

```
Cancelled Trains / Scheduled Trains
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** rail_transport
- **Sector:** rail

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 991 (batch 3)
