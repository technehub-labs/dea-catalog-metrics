# dea:metric-operational-loss-ratio

Candidate Performance Metric record for **Operational Loss Ratio** (OLR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-operational-loss-ratio`
- **Name:** Operational Loss Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** OLR

## 2. Definition

Operational Loss Ratio (OLR) addresses exposure to adverse outcomes and is a fixture of risk & compliance reporting. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Operational Losses / Revenue; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Operational losses - from error, fraud, external events, and process failure - as a share of revenue or of exposure measures. Its strategic weight is regulatory economics: under the Basel operational-risk framework, capital charges for operational risk have historically scaled with loss experience, which made this ratio a direct input to the cost of being a bank. The loss-event taxonomy from the Basel regime is what makes the metric comparable across institutions: internal fraud, external fraud, employment practices, clients and products, execution and delivery, and business disruption. The analysis that matters is by event type and severity: high-frequency low-severity losses indicate process quality problems, low-frequency high-severity losses indicate exposure and insurance questions, and the ratio blends them until separated. Also the metric where near-miss data earns its keep, since leading indicators are the only way to manage the tail.

## Formula

```
Operational Losses / Revenue
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** risk_compliance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 384 (batch 1)
