# dea:metric-logistics-cost-ratio

Candidate Performance Metric record for **Logistics Cost Ratio** (LCR-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-logistics-cost-ratio`
- **Name:** Logistics Cost Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LCR-S

## 2. Definition

Logistics Cost Ratio (LCR-S) measures how efficiently resources are converted into outputs in the Supply Chain domain. Its calculation is Total Logistics Cost / Revenue, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Total logistics spend - transport, warehousing, inventory carrying, and administration - as a share of revenue, the structural weight of moving things. Levels are industry destiny: heavy goods and remote geography push it up, compact high-value goods push it down, so it is read as trend and peer gap. Strategic use is decomposition: within the ratio, freight versus warehousing versus carrying cost move for different reasons, and optimizing one in isolation is the classic failure - cutting freight by consolidating shipments raises inventory and its carrying cost, which is exactly the trade-off this metric exists to expose. After disruptive freight cycles, the ratio becomes a pricing negotiation tool, since shippers benchmark their own number against published market rates to justify tenders.

## Formula

```
Total Logistics Cost / Revenue
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** supply_chain

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 183 (batch 1)
