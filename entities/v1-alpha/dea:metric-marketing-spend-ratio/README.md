# dea:metric-marketing-spend-ratio

Candidate Performance Metric record for **Marketing Spend Ratio** (MSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-marketing-spend-ratio`
- **Name:** Marketing Spend Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MSR

## 2. Definition

Marketing Spend Ratio (MSR) measures how efficiently resources are converted into outputs in the Marketing domain. The formula is Marketing Spend / Revenue - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Marketing expense as a share of revenue - the pacing metric that expresses how hard the growth pedal is pressed relative to the engine's output. Direct-to-consumer brands run near 30 percent in scale-up phase; enterprise software firms run near a tenth of that, and both can be optimal, which is why the ratio's value is trajectory rather than level. Strategically it is read against the acquisition funnel: a rising spend ratio with flat customer growth means saturation or creative fatigue; a falling ratio with maintained growth means brand pull or improving channel efficiency compounding in the company's favor. Boards use it as a sanity check on growth plans, since any projection implying stable CAC at rapidly increasing spend should have to defend it.

## Formula

```
Marketing Spend / Revenue
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** marketing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 112 (batch 1)
