# dea:metric-touchless-processing-rate

Candidate Performance Metric record for **Touchless Processing Rate** (TPR-G) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-touchless-processing-rate`
- **Name:** Touchless Processing Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TPR-G

## 2. Definition

Touchless Processing Rate (TPR-G) addresses how efficiently resources are converted into outputs and is a fixture of shared services & global business services reporting. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Transactions Processed without Manual Touch / Total Transactions, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Touchless processing rate measures the share of transactions flowing end-to-end without human intervention, and it is the automation-maturity metric of shared services - the difference between a process that requires someone to look at every transaction and one that handles exceptions only. The strategic logic is the exception-economics principle: the cost of a process is concentrated in its exceptions, so pushing routine volume to full automation moves the cost structure while the exception team focuses on the genuinely hard cases. The gaming risk is threshold-definition: an organization can define touchless as no-touch-in-this-system while manual work happens upstream (data entry, pre-validation) or downstream (error correction). Read with straight-through accuracy (automated transactions completed correctly versus requiring rework), exception-rate trend as the upstream driver, and cost per transaction which should validate the value capture.

## Formula

```
Transactions Processed without Manual Touch / Total Transactions
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** shared_services_global_business_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1056 (batch 4)
