# dea:metric-use-of-force-incident-rate

Candidate Performance Metric record for **Use-of-Force Incident Rate** (UOFIR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-use-of-force-incident-rate`
- **Name:** Use-of-Force Incident Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** UOFIR

## 2. Definition

Use-of-Force Incident Rate (UOFIR) captures exposure to adverse outcomes for organizations tracking security services & guarding. Its calculation is Use-of-Force Reports / 1,000 Shifts, measured in events per thousand or million (scaled). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. It originates from and is most used in Security practice.

## 3. Context

Measures force incidents per officer-shift or per site. It is the accountability metric of professional security: force incidents carry legal, contractual, and public-trust consequences, and officers trained in de-escalation generate dramatically fewer. Classification discipline matters - incident categories should be audited, since under-reporting is the standard failure. Read with training currency in de-escalation and complaint and litigation outcomes.

## Formula

```
Use-of-Force Reports / 1,000 Shifts
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** security_services_guarding
- **Sector:** security

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2058 (batch 6)
