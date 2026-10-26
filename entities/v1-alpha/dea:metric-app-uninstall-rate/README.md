# dea:metric-app-uninstall-rate

Candidate Performance Metric record for **App Uninstall Rate** (AUR-MOB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-app-uninstall-rate`
- **Name:** App Uninstall Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** AUR-MOB

## 2. Definition

A Mobile & Client Development indicator, App Uninstall Rate (AUR-MOB) quantifies the retention of customers, users, or assets over time. Its calculation is Uninstalls / Installs in Period, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. It originates from and is most used in Software practice.

## 3. Context

Measures the share of installs removed within a defined window. Uninstalls are a hard signal that onboarding or perceived value failed. Attribution between crash experience, size, and privacy concerns requires cohort analysis. Read with app store rating and day-30 retention rate.

## Formula

```
Uninstalls / Installs in Period
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** retention
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** mobile_client_development
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3263 (batch 7)
