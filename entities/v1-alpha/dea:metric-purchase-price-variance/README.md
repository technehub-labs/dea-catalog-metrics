# dea:metric-purchase-price-variance

Candidate Performance Metric record for **Purchase Price Variance** (PPV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-purchase-price-variance`
- **Name:** Purchase Price Variance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PPV

## 2. Definition

Purchase Price Variance (PPV) measures the economic value created or preserved in the Procurement domain. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is (Actual Price - Standard Price) x Quantity Purchased - reported in currency value. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the gap between standard and actual prices paid for purchased goods. It matters because it isolates procurement performance from volume and mix effects. Buyers can improve it cosmetically through slower deliveries or lower-quality substitutions that cost more downstream. Read with Supplier Defect Rate and Total Landed Cost to confirm price wins are not offset by quality or service losses.

## Formula

```
PPV = (Actual Price - Standard Price) x Quantity Purchased
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** procurement

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 221 (batch 1)
