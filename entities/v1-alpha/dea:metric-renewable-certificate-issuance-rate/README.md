# dea:metric-renewable-certificate-issuance-rate

Candidate Performance Metric record for **Renewable Certificate Issuance Rate** (RCIR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-renewable-certificate-issuance-rate`
- **Name:** Renewable Certificate Issuance Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RCIR

## 2. Definition

Renewable Certificate Issuance Rate (RCIR) captures conformance to standards, plans, or obligations for organizations tracking energy transition & renewables. The formula is Certificates Issued / Eligible Generation - reported in percent (%). It is a standard measure in the Renewable energy sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures certificates issued per unit of verified generation. It matters because certificates are the monetizable proof layer of renewable claims. Issuance mismatches with actual generation create integrity risk for the whole claims chain. Read with Generation Metering accuracy and certificate retirement practices to confirm issuance integrity.

## Formula

```
Certificates Issued / Eligible Generation
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** energy_transition_renewables
- **Sector:** renewable_energy

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1111 (batch 4)
