# dea:metric-hazardous-release-compliance-rate

Candidate Performance Metric record for **Hazardous Release Compliance Rate** (HRCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-hazardous-release-compliance-rate`
- **Name:** Hazardous Release Compliance Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** HRCR

## 2. Definition

Within Chemicals, Hazardous Release Compliance Rate (HRCR) is used to gauge conformance to standards, plans, or obligations. The formula is Releases within Permitted Limits / Release Events - reported in percent (%). It is a standard measure in the Chemicals sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Hazardous release compliance measures adherence to regulatory reporting, containment, and permit limits for chemical releases - the legal exposure metric covering emissions permits, TRI reporting, and release notification obligations. Compliance failures in chemicals carry outsized consequences beyond fines: criminal enforcement for knowing violations, community trust destruction, and permit revocation that can idle a plant entirely. The metric's blind spot is permitted-release creep: compliance can be 100 percent while permitted release volumes grow through permit amendments, which is a stakeholder-relations risk even when legally compliant. Read with permit exceedance trends by parameter, release reporting timeliness, community right-to-know disclosures, and toxic use reduction progress.

## Formula

```
HRCR = Releases within Permitted Limits / Release Events
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** chemicals
- **Sector:** chemicals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 899 (batch 3)
