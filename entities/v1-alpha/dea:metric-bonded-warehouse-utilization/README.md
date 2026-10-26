# dea:metric-bonded-warehouse-utilization

Candidate Performance Metric record for **Bonded Warehouse Utilization** (BWU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-bonded-warehouse-utilization`
- **Name:** Bonded Warehouse Utilization
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BWU

## 2. Definition

Bonded Warehouse Utilization (BWU) addresses the utilization or availability of capacity and is a fixture of international trade & customs reporting. The formula is Bonded Storage Used / Capacity - reported in percent (%). It is a standard measure in the Logistics & Trade sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Values outside the intended band, on either side, warrant investigation.

## Formula

```
Bonded Storage Used / Capacity
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1713 (batch 6)
