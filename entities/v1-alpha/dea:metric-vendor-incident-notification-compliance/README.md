# dea:metric-vendor-incident-notification-compliance

Candidate Performance Metric record for **Vendor Incident Notification Compliance** (VINC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-vendor-incident-notification-compliance`
- **Name:** Vendor Incident Notification Compliance
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** VINC

## 2. Definition

A Third-Party Risk Management indicator, Vendor Incident Notification Compliance (VINC) quantifies exposure to adverse outcomes. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Vendor Breaches Notified per Contract Terms / Breaches, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures whether vendors report security and continuity incidents within contracted windows. Late vendor notification blinds your response while their incident becomes yours. Compliance measured from vendor send-time rather than your awareness hides latency. Read with vendor security incident rate and mean time to detect - security.

## Formula

```
Vendor Breaches Notified per Contract Terms / Breaches
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** third_party_risk_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3724 (batch 8)
