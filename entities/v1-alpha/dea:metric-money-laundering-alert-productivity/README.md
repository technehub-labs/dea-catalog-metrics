# dea:metric-money-laundering-alert-productivity

Candidate Performance Metric record for **Money Laundering Alert Productivity** (MLAP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-money-laundering-alert-productivity`
- **Name:** Money Laundering Alert Productivity
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MLAP

## 2. Definition

Within Enterprise Fraud & Financial Crime Management, Money Laundering Alert Productivity (MLAP) is used to gauge the quality of outputs and outcomes. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Alerts Resulting in SAR / Alerts Generated - reported in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of AML alerts that convert to genuine cases. Productivity exposes the alert-noise problem that burns analyst capacity and buries true risks. Productivity rising through alert suppression rather than model improvement creates blind spots. Read with AML alert investigation cycle time and false positive rate (AML).

## Formula

```
Alerts Resulting in SAR / Alerts Generated
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** enterprise_fraud_financial_crime_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3771 (batch 8)
