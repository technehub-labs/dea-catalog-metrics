# dea:metric-sar-filing-timeliness-deep-dive

Candidate Performance Metric record for **SAR Filing Timeliness (Deep Dive)** (SFT-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-sar-filing-timeliness-deep-dive`
- **Name:** SAR Filing Timeliness (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SFT-D

## 2. Definition

Within Insurance Fraud & Financial Crime, SAR Filing Timeliness (Deep Dive) (SFT-D) is used to gauge conformance to standards, plans, or obligations. Its calculation is SARs Filed within Regulatory Deadline / SARs Due, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Financial Services practice.

## 3. Context

Measures suspicious-activity reports filed within regulatory deadlines. Timeliness is where AML programs fail audits: investigation backlogs push decisions past filing deadlines, converting good detection into late reporting, and regulators treat late SARs as control failures regardless of eventual quality. Clock definition (detection to filing) must match regulatory standards exactly. Read with investigation cycle times and backlog aging by risk tier.

## Formula

```
SARs Filed within Regulatory Deadline / SARs Due
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_fraud_financial_crime
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2472 (batch 6)
