# dea:metric-accessibility-compliance-rate-transit

Candidate Performance Metric record for **Accessibility Compliance Rate (Transit)** (ACR-T) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-accessibility-compliance-rate-transit`
- **Name:** Accessibility Compliance Rate (Transit)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ACR-T

## 2. Definition

A Public Transit indicator, Accessibility Compliance Rate (Transit) (ACR-T) quantifies conformance to standards, plans, or obligations. Its calculation is Stops and Vehicles Meeting Accessibility Standards / Total, measured in percent (%). It originates from and is most used in Public transit practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Accessibility compliance rate measures adherence to disability-access requirements - lifts, ramps, tactile guidance, audio announcements, accessible stations - and it is the metric where transit's legal obligations (ADA in the US and equivalents elsewhere) meet its social mission of universal mobility. Compliance is measurable and enforceable in ways satisfaction is not: station-by-station audits produce defensible status, and litigation risk concentrates precisely on non-compliance. The honest metric is journey-level rather than asset-level: a system can have compliant vehicles and compliant stations yet still strand a wheelchair user when an elevator is out of service, so operational availability (elevator/ lift uptime) is the lived-experience measure. Read with elevator and lift uptime, station accessibility share versus vehicle accessibility share, paratransit demand (which reflects mainline accessibility gaps), and complaint resolution for accessibility issues.

## Formula

```
Stops and Vehicles Meeting Accessibility Standards / Total
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** public_transit
- **Sector:** public_transit

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1006 (batch 3)
