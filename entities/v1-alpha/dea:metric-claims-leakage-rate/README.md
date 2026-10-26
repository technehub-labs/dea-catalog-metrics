# dea:metric-claims-leakage-rate

Candidate Performance Metric record for **Claims Leakage Rate** (CLR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-claims-leakage-rate`
- **Name:** Claims Leakage Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CLR

## 2. Definition

Claims Leakage Rate (CLR) captures the economic value created or preserved for organizations tracking claims operations (insurance). Its calculation is Claims Overpayment Value / Total Claims Paid, measured in percent (%). It originates from and is most used in Insurance practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Claims leakage measures payments beyond what proper claims handling would have required - overpayments, duplicate payments, unnecessary vendor costs, subrogation not pursued, and recovery opportunities missed. Industry studies put leakage at meaningful percentages of claim spend, making it one of the largest addressable cost pools in insurance operations. The measurement challenge is definitional: leakage requires knowing the correct payment, which is only established through audits and file reviews, so reported leakage depends entirely on audit scope and sampling rigor. The improvement levers differ by type: system-driven overpayments are fixable with technology, judgment-driven leakage (unnecessary vendor assignments) needs adjuster training and authority calibration. Read with audit-recovery rates, vendor-management metrics, and subrogation yield per claim.

## Formula

```
Claims Overpayment Value / Total Claims Paid
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** claims_operations_insurance
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 847 (batch 3)
