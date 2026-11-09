# dea:metric-digital-service-adoption

Candidate Performance Metric record for **Digital Service Adoption** (DSA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-digital-service-adoption`
- **Name:** Digital Service Adoption
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DSA

## 2. Definition

Within Public Sector & Government, Digital Service Adoption (DSA) is used to gauge how efficiently resources are converted into outputs. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Digital Channel Transactions / Total Transactions - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Public sector sector.

## 3. Context

The share of service transactions completed through digital channels - the transformation metric of digital government, and the one whose strategic significance is the cost-and-access trade it quantifies: digital channels cost a fraction of assisted ones and are available around the clock, and each point of adoption releases capacity and improves access simultaneously - the rare efficiency measure that is also an equity measure, for citizens who can use them. The honest analysis is by segment, because the adoption headline conceals who is adopting: high aggregate adoption built on the digital-comfortable population while the service-dependent (elderly, low-income, low-connectivity) remain on assisted channels creates a two-tier service whose aggregate metric looks excellent. Read with the assisted-channel cost trend: adoption that does not release assisted-channel capacity (because the remaining assisted users are the expensive ones) captures less savings than the migration arithmetic promised - the known economics of digital transition that the raw adoption rate overstates.

## Formula

```
DSA = Digital Channel Transactions / Total Transactions
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** public_sector_government
- **Sector:** public_sector

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 640 (batch 2)
