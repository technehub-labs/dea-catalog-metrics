# dea:metric-branch-transaction-digital-migration

Candidate Performance Metric record for **Branch Transaction Digital Migration** (BTDM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-branch-transaction-digital-migration`
- **Name:** Branch Transaction Digital Migration
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** BTDM

## 2. Definition

Branch Transaction Digital Migration (BTDM) captures how efficiently resources are converted into outputs for organizations tracking retail banking & lending. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Digitally Originated Transactions / Total Transactions, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Banking.

## 3. Context

Branch transaction digital migration measures the share of routine transactions moving from teller lines to digital channels, and it is the operating-cost pivot of retail banking - a teller transaction costs several dollars while a digital one costs cents, so migration is the mechanism that funds branch footprint rationalization. The metric's honesty problem is forced migration: pushing customers to digital by degrading branch service raises migration numbers while damaging relationships with segments who need branches, and closing branches before migration is genuinely complete strands revenue. The demographic split matters: migration success varies sharply by customer age and product complexity. Read with channel satisfaction by customer segment, branch cost-to-serve versus digital, and cross-sell rates by channel (branch interactions often carry higher relationship value).

## Formula

```
Digitally Originated Transactions / Total Transactions
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** retail_banking_lending
- **Sector:** banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 843 (batch 3)
