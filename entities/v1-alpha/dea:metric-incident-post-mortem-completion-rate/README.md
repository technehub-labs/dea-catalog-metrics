# dea:metric-incident-post-mortem-completion-rate

Candidate Performance Metric record for **Incident Post-Mortem Completion Rate** (IPMCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-incident-post-mortem-completion-rate`
- **Name:** Incident Post-Mortem Completion Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** IPMCR

## 2. Definition

Incident Post-Mortem Completion Rate (IPMCR) measures conformance to standards, plans, or obligations in the SecOps & Security Operations Center domain. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Incidents with Completed Post-Mortem / Major Incidents - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of qualifying security incidents with a completed, documented post-mortem. Learning loops are the only way incidents buy future capability. Completion measured as document filed, not actions owned, produces paperwork. Read with post-mortem action item closure rate and security incident recurrence rate.

## Formula

```
Incidents with Completed Post-Mortem / Major Incidents
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** secops_security_operations_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2784 (batch 7)
