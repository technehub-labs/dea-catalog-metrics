# dea:metric-api-enabled-business-exposure

Candidate Performance Metric record for **API-Enabled Business Exposure** (AEBE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-api-enabled-business-exposure`
- **Name:** API-Enabled Business Exposure
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** AEBE

## 2. Definition

API-Enabled Business Exposure (AEBE) addresses capability maturity or development and is a fixture of digital transformation reporting. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Services Exposed via APIs / Addressable Services, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of core business capabilities - products, pricing, logistics, data - made consumable by third parties through APIs, monetized directly or through partner ecosystems. It is the leading indicator of platform business models and embedded-finance style revenue pools. The trap is counting technical endpoints rather than valuable capabilities, and exposing APIs no partner uses. Read with partnership revenue share and developer or partner integration volume.

## Formula

```
AEBE = Services Exposed via APIs / Addressable Services
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** transformation
- **Purpose classification:** capability
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** digital_transformation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1316 (batch 5)
