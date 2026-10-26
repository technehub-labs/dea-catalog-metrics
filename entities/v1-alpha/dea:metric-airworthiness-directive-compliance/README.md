# dea:metric-airworthiness-directive-compliance

Candidate Performance Metric record for **Airworthiness Directive Compliance** (ADC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-airworthiness-directive-compliance`
- **Name:** Airworthiness Directive Compliance
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ADC

## 2. Definition

Within Aviation Maintenance Repair & Overhaul, Airworthiness Directive Compliance (ADC) is used to gauge conformance to standards, plans, or obligations. It is defined as Directives Implemented by Deadline / Directives Due; the result is stated in percent (%). In Airlines & aviation, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Airworthiness directive compliance measures completion of mandated corrective actions (inspections, modifications, replacements) that regulators issue when safety defects emerge, and it is the legal-safety floor of aviation maintenance: ADs are legally binding, and flying an aircraft past an AD deadline is a certificate-action offense with potential grounding. The metric's structure is deadline-critical rather than average-oriented: compliance rates mean little versus tracking items approaching deadline with engineering-extension mechanics (alternative means of compliance can be approved but are a regulated exception, not an option). Fleet-wide ADs (like the engine-inspection directives after high-profile engine-failure events) strain maintenance slots, requiring fleet planning trade-offs. Read with AD backlog aging, compliance plan adherence versus deadlines, engineering-approval documentation quality, and recurring non-compliance patterns which signal capacity rather than intent problems.

## Formula

```
Directives Implemented by Deadline / Directives Due
```

## Unit

- **Unit reference:** `dea:unit-percent`
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
- **Domain:** aviation_maintenance_repair_overhaul
- **Sector:** airlines_aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1189 (batch 4)
