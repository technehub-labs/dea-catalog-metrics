# dea:metric-overhead-ratio-nonprofit

Candidate Performance Metric record for **Overhead Ratio (Nonprofit)** (OHR-N) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-overhead-ratio-nonprofit`
- **Name:** Overhead Ratio (Nonprofit)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** OHR-N

## 2. Definition

A Nonprofit & NGO indicator, Overhead Ratio (Nonprofit) (OHR-N) quantifies how efficiently resources are converted into outputs. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is (Administrative + Fundraising Expenses) / Total Expenses - reported in percent (%). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Nonprofit & NGO sector.

## 3. Context

The nonprofit overhead ratio measures administrative and fundraising costs as a share of total expenses, and it is the sector's most quoted - and most misleading - efficiency metric. Its dysfunction is the starvation cycle: pressure to keep the ratio low drives underinvestment in systems, staff, and evaluation capacity, then miscoding of overhead costs into program lines to appear efficient, which leaves organizations hollow and misrepresents reality to donors. Charity raters have increasingly de-emphasized the ratio, acknowledging that impact per dollar is what matters and that overhead is frequently the investment that makes impact possible. Read with program-outcome metrics (the substance), infrastructure investment trend (is capacity being starved?), and honest cost classification rather than the ratio itself.

## Formula

```
(Administrative + Fundraising Expenses) / Total Expenses
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** nonprofit_ngo
- **Sector:** nonprofit_ngo

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1173 (batch 4)
