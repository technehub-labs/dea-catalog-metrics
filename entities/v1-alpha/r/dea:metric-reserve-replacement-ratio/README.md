# dea:metric-reserve-replacement-ratio

Candidate Performance Metric record for **Reserve Replacement Ratio** (RRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-reserve-replacement-ratio`
- **Name:** Reserve Replacement Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RRR

## 2. Definition

Reserve Replacement Ratio (RRR) addresses growth over time and is a fixture of oil & gas reporting. Its calculation is Reserves Added / Production, measured in ratio (x:1 or x). It originates from and is most used in Oil & gas practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Reserve replacement ratio measures newly added reserves divided by production - whether the company is replacing the barrels it extracts, with 100 percent the threshold for long-run viability and anything below 100 percent for multiple years signaling a shrinking business. The metric is easy to flatter through reserve revisions (price-driven reclassifications of known resources into proved reserves with no new discovery or capital) and through acquisitions, which replace reserves by purchase rather than exploration. Both are legitimate but different, which is why organic reserve replacement is the honester variant. Read with finding and development cost (replacement efficiency), revision-versus-discovery mix, SEC price-deck sensitivity of bookings, and reserve life index.

## Formula

```
RRR = Reserves Added / Production
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** oil_gas
- **Sector:** oil_gas

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 891 (batch 3)
