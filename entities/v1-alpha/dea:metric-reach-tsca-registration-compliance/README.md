# dea:metric-reach-tsca-registration-compliance

Candidate Performance Metric record for **REACH / TSCA Registration Compliance** (RTCC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-reach-tsca-registration-compliance`
- **Name:** REACH / TSCA Registration Compliance
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RTCC

## 2. Definition

REACH / TSCA Registration Compliance (RTCC) captures conformance to standards, plans, or obligations for organizations tracking chemicals & specialty materials. Its calculation is Substances with Current Registrations / Substances Handled, measured in percent (%). It originates from and is most used in Chemicals practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of substances and volumes compliant with chemical control regulations in relevant markets. Noncompliance halts sales at the border and creates enforcement exposure that scales with tonnage, and compliance horizons (registration, notification deadlines) demand lead-time management. Track by substance-tissue and by market, since obligations differ materially. Read with regulatory change intake and substance portfolio rationalization decisions.

## Formula

```
Substances with Current Registrations / Substances Handled
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** chemicals_specialty_materials
- **Sector:** chemicals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1820 (batch 6)
