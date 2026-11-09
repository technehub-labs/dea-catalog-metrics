# dea:metric-integration-count-per-application

Candidate Performance Metric record for **Integration Count per Application** (ICA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-integration-count-per-application`
- **Name:** Integration Count per Application
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ICA

## 2. Definition

Integration Count per Application (ICA) addresses capability maturity or development and is a fixture of enterprise architecture reporting. It is defined as Average Point-to-Point Interfaces per Application; the result is stated in ratio (x:1 or x). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the number of integrations connected to each application. It matters because integration density predicts change risk and retirement cost. Counting can miss undocumented integrations, understating true coupling. Read with Integration Debt assessment and application retirement feasibility to confirm coupling is understood.

## Formula

```
ICA = Average Point-to-Point Interfaces per Application
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** enterprise_architecture

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1349 (batch 5)
