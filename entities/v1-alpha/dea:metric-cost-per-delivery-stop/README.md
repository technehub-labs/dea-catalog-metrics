# dea:metric-cost-per-delivery-stop

Candidate Performance Metric record for **Cost per Delivery Stop** (CDS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-per-delivery-stop`
- **Name:** Cost per Delivery Stop
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CDS

## 2. Definition

Within Postal & Courier, Cost per Delivery Stop (CDS) is used to gauge how efficiently resources are converted into outputs. It is defined as Total Delivery Cost / Delivery Stops; the result is stated in currency per unit. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Lower values are better; each reduction is an improvement. In Postal & courier, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures average operating cost for each delivery stop on postal and courier routes. It matters because stop economics determine route viability, especially in rural service. Stops can be made cheaper by cutting service frequency, which trades cost for universal-service obligations. Read with On-Time Delivery Rate and Stops per Route to confirm efficiency coexists with service standards.

## Formula

```
Total Delivery Cost / Delivery Stops
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** postal_courier
- **Sector:** postal_courier

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 829 (batch 2)
