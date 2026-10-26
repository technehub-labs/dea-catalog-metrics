# dea:metric-realization-rate

Candidate Performance Metric record for **Realization Rate** (RLZ) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-realization-rate`
- **Name:** Realization Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RLZ

## 2. Definition

Realization Rate (RLZ) measures the economic value created or preserved in the Professional Services domain. It is computed as Fees Collected / Standard Fees Billed, expressed in percent (%). Its use is concentrated in Professional services. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Revenue actually collected (or billed without write-down) as a share of standard-rate value of hours worked - the leakage metric of the billable model, and the one that measures the difference between the work done and what the client paid for. Its strategic significance is the honesty it forces on the pricing conversation: firms that quote standard rates and routinely discount, write down, or lose hours to unbillable work are discounting through the back door, and the realization rate converts that scattered leakage into one number management can see. The measurement requires the discipline of recording time against engagement with rate structure intact, since realization cannot be measured on time never recorded. Read with the cause decomposition: write-downs by engagement type, client, and level show whether leakage is scoping (fixed-fee work exceeding budget), selling (rates promised too high), or delivery (hours exceeding value) - three different problems that require different fixes and that the blended rate never separates.

## Formula

```
RLZ = Fees Collected / Standard Fees Billed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** professional_services
- **Sector:** professional_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 680 (batch 2)
