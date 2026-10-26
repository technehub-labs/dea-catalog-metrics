# dea:metric-total-loss-frequency

Candidate Performance Metric record for **Total Loss Frequency** (TLF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-total-loss-frequency`
- **Name:** Total Loss Frequency
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TLF

## 2. Definition

Total Loss Frequency (TLF) addresses exposure to adverse outcomes and is a fixture of insurance claims deep dive reporting. The formula is Total Loss Settlements / Claims Settled - reported in percent (%). It is a standard measure in the Insurance sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Values outside the intended band, on either side, warrant investigation.

## Formula

```
Total Loss Settlements / Claims Settled
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_claims_deep_dive
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1562 (batch 6)
