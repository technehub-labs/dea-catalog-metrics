# dea:metric-cost-per-hire

Candidate Performance Metric record for **Cost per Hire** (CPH) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-per-hire`
- **Name:** Cost per Hire
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CPH

## 2. Definition

Cost per Hire (CPH) measures how efficiently resources are converted into outputs in the Human Resources domain. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Total Recruiting Cost / Hires, expressed in currency per unit. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures total recruiting cost divided by hires made. It matters because it benchmarks recruiting efficiency and informs sourcing mix decisions. Gaming risk includes excluding agency or referral fees, or deferring recruiting spend to cut the average. Read with Time to Fill and Quality of Hire to weigh efficiency against the downstream cost of bad hires.

## Formula

```
Total Recruiting Cost / Hires
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** organization
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** human_resources

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 134 (batch 1)
