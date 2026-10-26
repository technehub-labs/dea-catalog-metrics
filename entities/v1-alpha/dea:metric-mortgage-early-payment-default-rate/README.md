# dea:metric-mortgage-early-payment-default-rate

Candidate Performance Metric record for **Mortgage Early Payment Default Rate** (EPD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mortgage-early-payment-default-rate`
- **Name:** Mortgage Early Payment Default Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** EPD

## 2. Definition

Within Retail Banking & Lending, Mortgage Early Payment Default Rate (EPD) is used to gauge exposure to adverse outcomes. It is computed as Defaults within First Year / Loans Disbursed, expressed in percent (%). Its use is concentrated in Banking. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Mortgage early payment default rate measures borrowers going delinquent within the first months after origination, and it is the classic quality-control red flag for lenders - loans that default early almost always carry origination defects (misrepresented income, appraisal inflation, undisclosed debt), which is why EPD loans trigger repurchase obligations under GSE guidelines and why early-default clusters draw regulatory and investor scrutiny. EPD rate functions as an audit trigger and a credit-culture measure: a rising EPD rate suggests underwriting drift or fraud creeping into the channel. Read with repurchase demand counts from investors, first-payment default specifically (the sharpest defect signal), channel-level decomposition (correspondent versus wholesale versus retail), and fraud-detection hit rates by channel.

## Formula

```
Defaults within First Year / Loans Disbursed
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** retail_banking_lending
- **Sector:** banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 836 (batch 3)
