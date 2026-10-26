# dea:metric-commission-revenue-ratio

Candidate Performance Metric record for **Commission Revenue Ratio** (CRR-I) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-commission-revenue-ratio`
- **Name:** Commission Revenue Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CRR-I

## 2. Definition

Within Insurance Distribution & Brokerage, Commission Revenue Ratio (CRR-I) is used to gauge the economic value created or preserved. It is computed as Commission Revenue / Gross Written Premium, expressed in percent (%). Its use is concentrated in Insurance distribution. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Commission revenue ratio measures commission income as a share of total revenue in distribution, and it is the business-model-character metric - commission-heavy revenue models are transactional (grow when markets and deal activity grow) versus fee-for-service models which are advisory and durable, and the ratio positions a firm on that spectrum. The strategic debate the metric indexes is the industry's compensation-model transition: regulators and client pressure have pushed commission-based selling (with its conflict-of-interest structure) toward level-fee advice in multiple markets. The ratio also embeds product-mix economics - annuity and investment-product commissions carry different drag than pure protection products. Read with revenue per client trend (transactional models show declining per-client revenue between transactions), compensation-cost pass-through, and the compliance exposure of commission-driven sales conduct.

## Formula

```
Commission Revenue / Gross Written Premium
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_distribution_brokerage
- **Sector:** insurance_distribution

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1157 (batch 4)
