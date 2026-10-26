# dea:metric-same-store-sales-growth

Candidate Performance Metric record for **Same-Store Sales Growth** (SSSG) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-same-store-sales-growth`
- **Name:** Same-Store Sales Growth
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SSSG

## 2. Definition

Same-Store Sales Growth (SSSG) measures growth over time in the Franchise & Multi-site domain. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is (Comparable Store Sales_current - Sales_prior) / Sales_prior, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Franchise & multi-site practice.

## 3. Context

Same-store sales growth measures revenue change at locations open at least a year, and it is the franchising industry's core health metric - it isolates underlying demand from expansion, answering whether the concept works or whether growth is just new units. For franchisors specifically it matters twice: royalty revenue rides on franchisee sales, so system-wide comps are the franchisor's income statement. The gaming vector is well-known: price increases and reduced staffing both inflate comps while degrading customer experience, so comps without traffic and transaction decomposition hide value destruction. Read with customer traffic versus average ticket, franchisee margin trend (healthy comps with dying franchisees is a failing system), and unit-level profitability distribution.

## Formula

```
SSSG = (Comparable Store Sales_current - Sales_prior) / Sales_prior
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 804 (batch 2)
