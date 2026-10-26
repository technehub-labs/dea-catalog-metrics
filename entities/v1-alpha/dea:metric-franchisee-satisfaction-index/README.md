# dea:metric-franchisee-satisfaction-index

Candidate Performance Metric record for **Franchisee Satisfaction Index** (FSI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-franchisee-satisfaction-index`
- **Name:** Franchisee Satisfaction Index
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FSI

## 2. Definition

Franchisee Satisfaction Index (FSI) captures the engagement or satisfaction of the people involved for organizations tracking franchise & multi-site. It is computed as Weighted Franchisee Survey Score, expressed in index (0-100 or normalized). Its use is concentrated in Franchise & multi-site. It is reviewed at cadence by planning owners to correct course before issues become strategic. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures franchisee satisfaction with the franchisor relationship and support. It matters because franchisee economics drive system growth, renewal, and litigation risk. Surveying only top-performing or long-tenured franchisees skews the index high. Read with Franchise Unit Economics and Royalty Collection Rate to triangulate system health.

## Formula

```
FSI = Weighted Franchisee Survey Score
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** engagement
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 807 (batch 2)
