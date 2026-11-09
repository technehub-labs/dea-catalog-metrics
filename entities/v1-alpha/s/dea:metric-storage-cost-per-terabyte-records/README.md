# dea:metric-storage-cost-per-terabyte-records

Candidate Performance Metric record for **Storage Cost per Terabyte (Records)** (SCPT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-storage-cost-per-terabyte-records`
- **Name:** Storage Cost per Terabyte (Records)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SCPT

## 2. Definition

Storage Cost per Terabyte (Records) (SCPT) captures how efficiently resources are converted into outputs for organizations tracking records & information management. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Records Storage Spend / Terabytes Stored; the result is stated in currency per unit. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
SCPT = Records Storage Spend / Terabytes Stored
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** records_information_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3686 (batch 8)
