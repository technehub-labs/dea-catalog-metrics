# dea:metric-regulatory-submission-approval-rate

Candidate Performance Metric record for **Regulatory Submission Approval Rate** (RSAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-regulatory-submission-approval-rate`
- **Name:** Regulatory Submission Approval Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RSAR

## 2. Definition

Regulatory Submission Approval Rate (RSAR) measures how effectively a process or entity achieves its intended outcome in the Medical Devices domain. Its calculation is Submissions Approved without Major Deficiency / Submissions, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Medical devices practice.

## 3. Context

Regulatory submission approval rate measures the share of FDA/CE/other regulatory filings approved without major deficiencies or resubmission cycles, and it is the industry's gatekeeper metric - each resubmission adds 6 to 12 months of revenue delay for products with finite patent life. The diagnostic value lies in the deficiency pattern: repeated deficiencies on the same technical area signal a systemic evidence-generation gap, not a one-off filing issue. The metric also embeds strategy choices - a 513(f) de novo strategy trades approval rate for speed in some cases. Read with cycle-time distribution and first-cycle approval rate by submission type.

## Formula

```
RSAR = Submissions Approved without Major Deficiency / Submissions
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** medical_devices
- **Sector:** medical_devices

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 761 (batch 2)
