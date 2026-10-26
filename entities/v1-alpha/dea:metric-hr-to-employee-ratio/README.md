# dea:metric-hr-to-employee-ratio

Candidate Performance Metric record for **HR to Employee Ratio** (HRER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-hr-to-employee-ratio`
- **Name:** HR to Employee Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** HRER

## 2. Definition

HR to Employee Ratio (HRER) captures how efficiently resources are converted into outputs for organizations tracking human resources. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as HR FTEs / Total Employee FTEs; the result is stated in ratio (x:1 or x). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures HR staff per 100 employees. It matters as a benchmark of HR function sizing and a check on whether service delivery is being starved. It can be gamed by outsourcing transactional HR work, which hides the true support cost inside vendor invoices. Read with HR Service Delivery Satisfaction and Absence Rate to judge whether lean ratios are efficient or just stretched.

## Formula

```
HRER = HR FTEs / Total Employee FTEs
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** organization
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** human_resources

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 138 (batch 1)
