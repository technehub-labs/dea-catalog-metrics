# dea:metric-predictive-maintenance-resolution-rate

Candidate Performance Metric record for **Predictive Maintenance Resolution Rate** (PMRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-predictive-maintenance-resolution-rate`
- **Name:** Predictive Maintenance Resolution Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PMRR

## 2. Definition

Predictive Maintenance Resolution Rate (PMRR) captures the quality of outputs and outcomes for organizations tracking telecom network operations. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Issues Resolved before Failure via Prediction / Predicted Issues, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Telecommunications.

## 3. Context

Measures how effectively predicted network faults are resolved before failure. It matters because proactive fixes avoid customer-impacting outages at far lower cost. Teams can inflate it by counting routine replacements as predictive saves. Read with Unplanned Outage Rate and False Alarm Rate to confirm predictions convert to avoided failures.

## Formula

```
Issues Resolved before Failure via Prediction / Predicted Issues
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** telecom_network_operations
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 859 (batch 3)
