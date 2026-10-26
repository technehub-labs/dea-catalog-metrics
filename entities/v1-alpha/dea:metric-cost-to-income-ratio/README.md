# dea:metric-cost-to-income-ratio

Candidate Performance Metric record for **Cost-to-Income Ratio** (CIR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-to-income-ratio`
- **Name:** Cost-to-Income Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CIR

## 2. Definition

Cost-to-Income Ratio (CIR) captures how efficiently resources are converted into outputs for organizations tracking banking & financial services. It is computed as Operating Expenses / Operating Income, expressed in ratio (x:1 or x). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is concentrated in Financial services.

## 3. Context

Operating expenses over operating income - the banking sectors efficiency benchmark, tracked obsessively in European bank coverage because it compresses the whole cost story into one figure. A ratio below 50 percent is generally considered efficient; above 60 percent raises structural questions about over-branching, legacy technology, or an income line too thin to carry the platform. Its trap is the denominator: in a downturn, falling income mechanically worsens the ratio even with disciplined costs, so banks that cut expenses into a weak revenue environment can look worse before they look better. The honest read separates structural costs (the ones that need investment to remove) from discretionary ones, and tracks the ratio through a full rate cycle before declaring success.

## Formula

```
Operating Expenses / Operating Income
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 36 (batch 1)
