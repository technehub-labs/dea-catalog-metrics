# dea:metric-compensation-ratio-to-market

Candidate Performance Metric record for **Compensation Ratio to Market** (CRM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-compensation-ratio-to-market`
- **Name:** Compensation Ratio to Market
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CRM

## 2. Definition

Compensation Ratio to Market (CRM) addresses the economic value created or preserved and is a fixture of human resources reporting. It is computed as Average Salary / Market Median Salary, expressed in ratio (x:1 or x). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Organization pay levels relative to the market benchmark - typically the ratio of company median pay to market median for matched roles, the control variable of the entire compensation strategy. Its strategic content is positioning: paying at market with strong engagement is efficiency; paying above market while losing talent signals the problem is not money but management or work design. The metric is read in distribution, not average - a company at 1.0 on average with a long left tail is overpaying the market for some roles and losing its best people in others, a pattern that only percentile-band analysis reveals. The comparison integrity depends on the survey cut: matching the right industry, size band, and geography matters more than the precision of the ratio itself.

## Formula

```
CRM = Average Salary / Market Median Salary
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** organization
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** human_resources

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 143 (batch 1)
