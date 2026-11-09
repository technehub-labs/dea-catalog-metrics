# dea:metric-security-clearance-processing-time

Candidate Performance Metric record for **Security Clearance Processing Time** (SCPT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-security-clearance-processing-time`
- **Name:** Security Clearance Processing Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SCPT

## 2. Definition

Within Defense & Aerospace, Security Clearance Processing Time (SCPT) is used to gauge how efficiently resources are converted into outputs. It is computed as Days from Clearance Request to Adjudication, expressed in days. It is reviewed at cadence by planning owners to correct course before issues become strategic. Lower values are better; each reduction is an improvement. Its use is concentrated in Defense & aerospace.

## 3. Context

Measures elapsed time from clearance application to adjudication. It matters because clearance delay bottlenecks staffing for classified programs, and cleared-personnel scarcity is a market constraint. Time can be gamed by counting only clean cases and deferring complex ones into a backlog outside the metric. Read with Backlog of Pending Cases for clearances and program staffing vacancy data to see the whole picture.

## Formula

```
SCPT = Days from Clearance Request to Adjudication
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** defense_aerospace
- **Sector:** defense_aerospace

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 973 (batch 3)
