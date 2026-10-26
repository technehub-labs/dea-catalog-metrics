# dea:metric-privacy-breach-notification-timeliness

Candidate Performance Metric record for **Privacy Breach Notification Timeliness** (PBNT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-privacy-breach-notification-timeliness`
- **Name:** Privacy Breach Notification Timeliness
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PBNT

## 2. Definition

Privacy Breach Notification Timeliness (PBNT) addresses exposure to adverse outcomes and is a fixture of data privacy & protection reporting. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Breaches Notified to Regulator within Deadline / Notifiable Breaches - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures whether personal data breaches are notified to regulators and individuals within required windows. Notification failures compound a breach into an enforcement case. Timeliness measured from internal detection rather than awareness start cuts corners. Read with breach response readiness and mean time to detect - security.

## Formula

```
Breaches Notified to Regulator within Deadline / Notifiable Breaches
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** data_privacy_protection

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3663 (batch 8)
