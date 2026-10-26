# dea:metric-privacy-consent-compliance-rate

Candidate Performance Metric record for **Privacy Consent Compliance Rate** (PCCR-A) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-privacy-consent-compliance-rate`
- **Name:** Privacy Consent Compliance Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PCCR-A

## 2. Definition

Privacy Consent Compliance Rate (PCCR-A) addresses conformance to standards, plans, or obligations and is a fixture of customer analytics & insights reporting. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Profiles with Valid Marketing Consent / Profiles Marketed - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of customer data processing and marketing activity for which valid, current, purpose-matched consent exists. Beyond regulatory exposure, consent gaps degrade data quality by forcing record exclusion mid-campaign. Measure by processing purpose rather than by record, and remember consent expiry and withdrawal flows, which are where programs quietly fail. Read with customer data platform coverage for the usable-data reality.

## Formula

```
Profiles with Valid Marketing Consent / Profiles Marketed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** customer_analytics_insights

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1429 (batch 5)
