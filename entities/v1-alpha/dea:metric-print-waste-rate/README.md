# dea:metric-print-waste-rate

Candidate Performance Metric record for **Print Waste Rate** (PWR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-print-waste-rate`
- **Name:** Print Waste Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PWR

## 2. Definition

Print Waste Rate (PWR) addresses how efficiently resources are converted into outputs and is a fixture of printing & publishing reporting. Its calculation is Wasted Sheets / Total Sheets Consumed, measured in percent (%). It originates from and is most used in Printing & publishing practice. It provides the day-to-day signal that a process is running as designed. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Wasted Sheets / Total Sheets Consumed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** printing_publishing
- **Sector:** printing_publishing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1260 (batch 4)
