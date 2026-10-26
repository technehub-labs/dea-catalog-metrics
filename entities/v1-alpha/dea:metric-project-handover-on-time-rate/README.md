# dea:metric-project-handover-on-time-rate

Candidate Performance Metric record for **Project Handover On-Time Rate** (PHOT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-project-handover-on-time-rate`
- **Name:** Project Handover On-Time Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PHOT

## 2. Definition

Project Handover On-Time Rate (PHOT) captures conformance to standards, plans, or obligations for organizations tracking construction & engineering. The formula is Projects Handed Over on Schedule / Projects Completed - reported in percent (%). It is a standard measure in the Construction & engineering sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The share of projects formally handed over to the client by the contractual date - the completion-side delivery metric of construction, and the one the client remembers: progress payments, logistics, and reputation are all built against the handover date, and construction contracts typically carry liquidated damages that convert late handover directly into cost. Its strategic significance is the extension-cascade risk: handover delays on one project consume supervisory staff and equipment needed on the next, converting a single late project into a portfolio effect - which is why contractors watch handover concentration by quarter. The honest read is against the contractual machinery: claims, variations, and force-majeure events move the contractual date, so the metric is only meaningful tracked against the contract as amended - and a contractor whose on-time rate is achieved through extensive variation orders has delivered punctuality for a different project than was sold. Read with the quality-at-handover companion: snag-free handovers versus handovers with long defect lists are different products wearing the same date.

## Formula

```
Projects Handed Over on Schedule / Projects Completed
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** construction_engineering
- **Sector:** construction_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 673 (batch 2)
