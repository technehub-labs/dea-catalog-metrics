# dea:metric-net-stable-funding-ratio

Candidate Performance Metric record for **Net Stable Funding Ratio** (NSFR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-net-stable-funding-ratio`
- **Name:** Net Stable Funding Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** NSFR

## 2. Definition

Net Stable Funding Ratio (NSFR) addresses exposure to adverse outcomes and is a fixture of banking & financial services reporting. It is computed as Available Stable Funding / Required Stable Funding, expressed in ratio (x:1 or x). Its use is concentrated in Financial services. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The Basel III structural liquidity counterpart to the LCR: available stable funding over required stable funding, measured over a one-year horizon rather than 30 days. Where the LCR prevents a short-term run from becoming a fire sale, the NSFR attacks the maturity mismatch that caused runs in the first place, by assigning funding sources stability weights (retail deposits score high, short-term wholesale scores low) and requiring assets to be backed by funding of comparable stickiness. Its effect on bank behavior has been concrete: term funding issuance rose, securities financing shortened, and the price of unstable funding rose accordingly. Banks near 100 percent are structurally sound but may be overpaying for funding - the optimization frontier, not the minimum, is the strategic question.

## Formula

```
Available Stable Funding / Required Stable Funding
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** banking_financial_services
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 42 (batch 1)
