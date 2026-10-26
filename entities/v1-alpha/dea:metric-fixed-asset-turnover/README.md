# dea:metric-fixed-asset-turnover

Candidate Performance Metric record for **Fixed Asset Turnover** (FAT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fixed-asset-turnover`
- **Name:** Fixed Asset Turnover
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FAT

## 2. Definition

Fixed Asset Turnover (FAT) addresses how efficiently resources are converted into outputs and is a fixture of finance & accounting reporting. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Revenue / Net Fixed Assets, measured in ratio (x:1 or x). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures revenue generated per unit of net fixed assets. It matters as a read on how hard the asset base is working to produce sales. Selling productive assets right before period end temporarily lifts the ratio while hollowing out future capacity. Read with Return on Assets and Capacity Utilization to distinguish productive leverage from asset starvation.

## Formula

```
Revenue / Net Fixed Assets
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** finance_accounting

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 33 (batch 1)
