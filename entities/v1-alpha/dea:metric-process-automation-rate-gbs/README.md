# dea:metric-process-automation-rate-gbs

Candidate Performance Metric record for **Process Automation Rate (GBS)** (PAR-G) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-process-automation-rate-gbs`
- **Name:** Process Automation Rate (GBS)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PAR-G

## 2. Definition

Process Automation Rate (GBS) (PAR-G) captures capability maturity or development for organizations tracking shared services & global business services. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Automated Process Steps / Total Process Steps, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Process automation rate in global business services measures the share of process volume executed through automated workflows, robotic process automation, or AI-assisted handling, and it is the transformation-progress metric of the GBS agenda. The honest measurement issue is definitional honesty: RPA and true process redesign differ fundamentally in durability (RPA layers fragile screen-based automation on top of a bad process; redesign fixes the process itself), and both count as automation in a naive rate. The value-capture test is what matters: automation that reduces handling time without reducing cost (automation plus parallel manual verification) captures nothing. The second-order effect is capacity: freed human capacity should move to judgment-work, not just disappear into unfunded effort. Read with cost per transaction trend as the value-capture validation, exception-rate changes (automation shifts failure modes), and benefit-realization tracking against business case.

## Formula

```
Automated Process Steps / Total Process Steps
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capability
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1062 (batch 4)
