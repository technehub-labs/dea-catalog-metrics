# dea:metric-cost-to-originate

Candidate Performance Metric record for **Cost to Originate** (CTO) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-to-originate`
- **Name:** Cost to Originate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CTO

## 2. Definition

Cost to Originate (CTO) measures how efficiently resources are converted into outputs in the Retail Banking & Lending domain. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Total Origination Cost / Loans Originated, expressed in currency per unit. It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Banking.

## 3. Context

Cost to originate measures all expenses of producing a loan - staffing, technology, appraisal, credit, marketing - divided by funded volume, and it is the structural pain point of consumer lending: industry benchmarks have run around $8,000-plus per mortgage in recent years, far above what digital-first transformation was supposed to deliver. The metric embeds both fixed-cost allocation and volume cyclicality, which cuts both ways: in low-rate years, volume spreads fixed costs thin, and in high-rate years volume collapse inflates unit costs. Gaming risk is definitional - excluding marketing or commissions lowers the number without changing economics. Read with pull-through rate (cost per funded loan versus per application), cycle time (cost sits in queues), and productivity metrics per FTE.

## Formula

```
Total Origination Cost / Loans Originated
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 840 (batch 3)
