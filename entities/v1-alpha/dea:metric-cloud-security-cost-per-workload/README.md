# dea:metric-cloud-security-cost-per-workload

Candidate Performance Metric record for **Cloud Security Cost per Workload** (CSCW) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cloud-security-cost-per-workload`
- **Name:** Cloud Security Cost per Workload
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CSCW

## 2. Definition

Cloud Security Cost per Workload (CSCW) addresses how efficiently resources are converted into outputs and is a fixture of cloud security posture management reporting. It is defined as Annual Cloud Security Spend / Managed Workloads; the result is stated in currency per unit. It is applied across virtually every sector. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
CSCW = Annual Cloud Security Spend / Managed Workloads
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** risk
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** cloud_security_posture_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3321 (batch 7)
