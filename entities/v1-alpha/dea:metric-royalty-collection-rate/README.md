# dea:metric-royalty-collection-rate

Candidate Performance Metric record for **Royalty Collection Rate** (RCR-F) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-royalty-collection-rate`
- **Name:** Royalty Collection Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RCR-F

## 2. Definition

Royalty Collection Rate (RCR-F) addresses conformance to standards, plans, or obligations and is a fixture of franchise & multi-site reporting. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Royalties Collected / Royalties Owed, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Franchise & multi-site.

## 3. Context

Measures the share of royalties due that are actually collected. It matters because leakage is a direct hit to franchisor revenue and signals audit discipline. Under-collection often hides in unverified self-reported franchisee revenue. Read with Franchisee Audit findings and Revenue Reporting accuracy to confirm collections reflect true sales.

## Formula

```
Royalties Collected / Royalties Owed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** franchise_multi_site
- **Sector:** franchise_multi_site

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 808 (batch 2)
