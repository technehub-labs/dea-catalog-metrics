# dea:metric-charge-off-rate

Candidate Performance Metric record for **Charge-Off Rate** (COR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-charge-off-rate`
- **Name:** Charge-Off Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** COR

## 2. Definition

Charge-Off Rate (COR) measures exposure to adverse outcomes in the Banking & Financial Services domain. It is computed as Net Charge-Offs / Average Loans Outstanding, expressed in percent (%). Its use is concentrated in Financial services. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

The portion of the loan book written off as uncollectible over a period, net of recoveries - the point where credit risk stops being a provision and becomes a realized loss. Unlike delinquency ratios, which are early warnings, charge-offs are the settled account of underwriting quality, which is why they anchor lifetime loss estimates in IFRS 9 and CECL models. Strategic use is the vintage view: charging off a bad vintage confirms what the delinquency curve showed years earlier, so cohort analysis reveals whether elevated charge-offs are a passing cohort or a widening funnel. The recovery netting is where comparability dies - secured books with collateral recover slowly, and institutions differ on when they declare a loss dead.

## Formula

```
COR = Net Charge-Offs / Average Loans Outstanding
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** banking_financial_services
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 47 (batch 1)
