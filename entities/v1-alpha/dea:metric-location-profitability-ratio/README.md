# dea:metric-location-profitability-ratio

Candidate Performance Metric record for **Location Profitability Ratio** (LPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-location-profitability-ratio`
- **Name:** Location Profitability Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** LPR

## 2. Definition

Location Profitability Ratio (LPR) addresses the economic value created or preserved and is a fixture of franchise & multi-site reporting. It is computed as Profitable Locations / Total Locations, expressed in percent (%). Its use is concentrated in Franchise & multi-site. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Location profitability ratio compares unit-level profit against system benchmarks or corporate targets, and it is the portfolio-management view of a multi-site business - the distribution matters more than the average, since a chain is really a portfolio of local monopolies with individually determined economics. The diagnostic value comes from decomposing variance: is underperformance driven by revenue (location, competition, brand awareness) or cost (rent, labor market, management quality)? Each requires different intervention. Watch for allocation distortions - corporate overhead allocation can mask which units truly work. Read with the full percentile distribution of unit margins, management-tenure versus profitability correlation, and location closure/relocation decisions as revealed preference.

## Formula

```
Profitable Locations / Total Locations
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** franchise_multi_site
- **Sector:** franchise_multi_site

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 810 (batch 2)
