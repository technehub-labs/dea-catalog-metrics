# dea:metric-port-state-control-detention-rate-deep-dive

Candidate Performance Metric record for **Port State Control Detention Rate (Deep Dive)** (PSCDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-port-state-control-detention-rate-deep-dive`
- **Name:** Port State Control Detention Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PSCDR

## 2. Definition

Within Maritime Shipping (Deep Dive), Port State Control Detention Rate (Deep Dive) (PSCDR) is used to gauge conformance to standards, plans, or obligations. It is computed as Detentions / Inspections, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is concentrated in Maritime.

## 3. Context

Measures ships detained at foreign port inspections. Detentions are the operational and reputational scarlet letter of maritime safety: they strand schedules, trigger class and flag scrutiny, and concentrate insurance attention, and repeat detention patterns invite blacklisting. Deficiency root-cause closure determines whether the rate stays down. Read with deficiency trends by inspection port and class survey findings.

## Formula

```
Detentions / Inspections
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** maritime_shipping_deep_dive
- **Sector:** maritime

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2437 (batch 6)
