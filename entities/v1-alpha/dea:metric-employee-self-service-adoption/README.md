# dea:metric-employee-self-service-adoption

Candidate Performance Metric record for **Employee Self-Service Adoption** (ESSA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-employee-self-service-adoption`
- **Name:** Employee Self-Service Adoption
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ESSA

## 2. Definition

Employee Self-Service Adoption (ESSA) captures how efficiently resources are converted into outputs for organizations tracking shared services & global business services. It is computed as Transactions Completed by Employees via Self-Service / Total Transactions, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Employee self-service adoption measures the share of transactions employees complete themselves - expense submission, leave requests, address changes, payslip access - rather than through shared-services or HR staff, and it is the demand-side efficiency metric of service models: an organization can automate the back office completely and still burn cost if employees call to ask what they could self-serve. The gaming risk mirrors all adoption metrics: adoption achieved by degrading assisted-service channels (slow response, hidden contact routes) inflates the number while harming employees who genuinely need help, so adoption must be paired with experience scores. The sophistication arc is real: mature implementations move from transaction self-service to employee-empowerment (self-service analytics, tools that answer policy questions rather than route them to experts). Read with containment rate (self-service attempts that would have become calls), assisted-channel satisfaction, and adoption by employee segment (field versus office workers differ sharply).

## Formula

```
ESSA = Transactions Completed by Employees via Self-Service / Total Transactions
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1061 (batch 4)
