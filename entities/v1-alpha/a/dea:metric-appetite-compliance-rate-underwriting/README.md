# dea:metric-appetite-compliance-rate-underwriting

Candidate Performance Metric record for **Appetite Compliance Rate (Underwriting)** (ACR-U) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-appetite-compliance-rate-underwriting`
- **Name:** Appetite Compliance Rate (Underwriting)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ACR-U

## 2. Definition

Within Insurance Underwriting, Appetite Compliance Rate (Underwriting) (ACR-U) is used to gauge conformance to standards, plans, or obligations. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Risks Written within Appetite Guidelines / Risks Written, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Insurance.

## 3. Context

Measures the share of written business that conforms to the stated underwriting appetite and risk guidelines. Non-compliant writes concentrate precisely where discipline failed under growth pressure, and the metric makes that visible before losses emerge. Compliance judged at submission understates drift versus point-of-sale checks, and appetite statements must be specific enough to test or the metric is decorative. Read with underwriting authority exception rates and loss ratio by compliance cohort.

## Formula

```
ACR-U = Risks Written within Appetite Guidelines / Risks Written
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_underwriting
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1511 (batch 6)
