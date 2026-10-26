# dea:metric-device-defect-rate

Candidate Performance Metric record for **Device Defect Rate** (DDR-MD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-device-defect-rate`
- **Name:** Device Defect Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DDR-MD

## 2. Definition

Within Medical Devices, Device Defect Rate (DDR-MD) is used to gauge exposure to adverse outcomes. Its calculation is Reported Device Defects / Devices Shipped, measured in percent (%). It originates from and is most used in Medical devices practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Device defect rate tracks the share of medical devices failing quality checks or being returned as defective, and in medtech a defect is not just a cost issue but a patient-safety and regulatory one, since a pattern of defects can trigger a design re-review or consent decree from the FDA. The measurement subtlety is severity weighting: a cosmetic surface flaw and a mislabeled device count the same in a raw rate despite completely different risk profiles. Read alongside complaint rate, which surfaces field performance in actual clinical use, and MDR (medical device report) submissions, which are the regulatory early-warning channel.

## Formula

```
Reported Device Defects / Devices Shipped
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** medical_devices
- **Sector:** medical_devices

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 752 (batch 2)
