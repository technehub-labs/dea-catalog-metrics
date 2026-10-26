# dea:metric-soc-cost-per-investigated-incident

Candidate Performance Metric record for **SOC Cost per Investigated Incident** (SOCPII) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-soc-cost-per-investigated-incident`
- **Name:** SOC Cost per Investigated Incident
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SOCPII

## 2. Definition

SOC Cost per Investigated Incident (SOCPII) addresses how efficiently resources are converted into outputs and is a fixture of secops & security operations center reporting. It is defined as SOC Operating Cost / Investigated Incidents; the result is stated in currency value. Its trend is watched by senior leadership as an early signal of structural performance shifts. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the fully loaded cost of operating the SOC divided by investigated incidents. It frames security operations as a managed unit cost while flagging alert fatigue. Costs rise faster than risk if triage automation lags, but cutting costs by ignoring low-severity alerts creates blind spots. Read with mean time to respond - security and analyst attrition rate - SOC.

## Formula

```
SOC Operating Cost / Investigated Incidents
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** secops_security_operations_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2796 (batch 7)
