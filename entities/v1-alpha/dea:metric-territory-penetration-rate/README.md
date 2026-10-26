# dea:metric-territory-penetration-rate

Candidate Performance Metric record for **Territory Penetration Rate** (TPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-territory-penetration-rate`
- **Name:** Territory Penetration Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** TPR

## 2. Definition

Within Franchise & Multi-site, Territory Penetration Rate (TPR) is used to gauge growth over time. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Active Franchised Territories / Addressable Territories - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Franchise & multi-site sector.

## 3. Context

Territory penetration rate measures market share of the addressable opportunity within a defined territory, and it is the expansion-discipline metric for franchised and distributed systems - territories with low penetration may be underexploited or simply weak, and the distinction requires local demand analysis. The measurement honesty depends on addressable-market definition: a territory drawn too broadly makes penetration look hopeless and justifies underinvestment; too narrow and it flatters. Penetration also interacts with density economics - delivery, advertising, and supervision costs all improve with density, so penetration gains near existing units are worth more than remote ones. Read with per-territory unit economics, competitor density, and demographic fit of territory boundaries.

## Formula

```
Active Franchised Territories / Addressable Territories
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** growth
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 813 (batch 2)
