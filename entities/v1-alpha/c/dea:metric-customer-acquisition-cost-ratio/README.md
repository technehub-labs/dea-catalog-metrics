# dea:metric-customer-acquisition-cost-ratio

Candidate Performance Metric record for **Customer Acquisition Cost Ratio** (CACR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-customer-acquisition-cost-ratio`
- **Name:** Customer Acquisition Cost Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CACR

## 2. Definition

Customer Acquisition Cost Ratio (CACR) captures the economic value created or preserved for organizations tracking marketing. Its calculation is CAC / Average Customer Lifetime Value, measured in ratio (x:1 or x). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Customer acquisition cost expressed relative to the value it acquires - conventionally against customer lifetime value, giving the CAC-to-LTV shorthand that governs growth-capital allocation. Where raw CAC is an absolute, the ratio is self-calibrating across price points and markets, which is what makes it the go/no-go number for scaling spend: a ratio implying 12-month payback supports aggressive investment, one implying 5-year payback requires retention proof before scaling. The strategic trap is the input correlation - LTV computed from the cohorts the current CAC bought circularly rewards whatever was bought, so the ratio must be refreshed from realized cohort behavior, not model lifetime value, whenever the mix or price changes.

## Formula

```
CACR = CAC / Average Customer Lifetime Value
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** marketing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 111 (batch 1)
