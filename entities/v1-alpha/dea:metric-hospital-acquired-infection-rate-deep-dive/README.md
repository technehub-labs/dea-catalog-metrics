# dea:metric-hospital-acquired-infection-rate-deep-dive

Candidate Performance Metric record for **Hospital-Acquired Infection Rate (Deep Dive)** (HAI-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-hospital-acquired-infection-rate-deep-dive`
- **Name:** Hospital-Acquired Infection Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** HAI-D

## 2. Definition

A Medical Practice & Clinical Operations indicator, Hospital-Acquired Infection Rate (Deep Dive) (HAI-D) quantifies exposure to adverse outcomes. Its calculation is HAIs / Device or Admission Days, measured in events per thousand or million (scaled). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. It originates from and is most used in Healthcare practice.

## 3. Context

Measures infections originating in care - CLABSI, CAUTI, surgical site, C. difficile - typically per device-day or procedure. HAIs are the purest preventable-harm metric: they are largely process-failures (hygiene, device management) with patient costs and payment penalties attached. Device utilization ratios belong alongside the rates, since infections per line-day conceal overuse of devices themselves. Read with hand hygiene compliance and device utilization trends.

## Formula

```
HAIs / Device or Admission Days
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** medical_practice_clinical_operations
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1647 (batch 6)
