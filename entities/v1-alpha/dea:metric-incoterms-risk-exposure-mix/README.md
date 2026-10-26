# dea:metric-incoterms-risk-exposure-mix

Candidate Performance Metric record for **Incoterms Risk Exposure Mix** (IREM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-incoterms-risk-exposure-mix`
- **Name:** Incoterms Risk Exposure Mix
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** IREM

## 2. Definition

Incoterms Risk Exposure Mix (IREM) addresses exposure to adverse outcomes and is a fixture of international trade & customs reporting. It is computed as Shipment Value by Incoterms Risk-Transfer Point, expressed in percent (%). Its use is concentrated in Logistics & Trade. It is reviewed at cadence by planning owners to correct course before issues become strategic. Values outside the intended band, on either side, warrant investigation.

## Formula

```
Shipment Value by Incoterms Risk-Transfer Point
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** international_trade_customs
- **Sector:** logistics_trade

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1721 (batch 6)
