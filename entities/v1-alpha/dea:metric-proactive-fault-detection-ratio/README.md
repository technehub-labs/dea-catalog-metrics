# dea:metric-proactive-fault-detection-ratio

Candidate Performance Metric record for **Proactive Fault Detection Ratio** (PFDR-N) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-proactive-fault-detection-ratio`
- **Name:** Proactive Fault Detection Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PFDR-N

## 2. Definition

Within Telecom Network Operations (Deep Dive), Proactive Fault Detection Ratio (PFDR-N) is used to gauge capability maturity or development. Its calculation is Faults Detected Proactively / Total Faults, measured in percent (%). It originates from and is most used in Telecommunications practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of faults detected by monitoring and prediction before customers report. It is the maturity metric of network operations: proactive detection typically costs an order of magnitude less than customer-reported failures, and it converts NOC operations from firefighting to prevention. Detection that alerts after the customer has already noticed is fake proactivity. Read with network availability (Deep Dive) and mean time to detect versus repair trends.

## Formula

```
Faults Detected Proactively / Total Faults
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** telecom_network_operations_deep_dive
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2134 (batch 6)
