# dea:metric-cost-per-citizen-served

Candidate Performance Metric record for **Cost per Citizen Served** (CPCS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-per-citizen-served`
- **Name:** Cost per Citizen Served
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CPCS

## 2. Definition

Within Public Sector & Government, Cost per Citizen Served (CPCS) is used to gauge how efficiently resources are converted into outputs. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Total Service Delivery Cost / Citizens Served - reported in currency per unit. It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Public sector sector.

## 3. Context

Total program or service cost divided by citizens served - the unit-cost metric of public service delivery, and the one that makes the efficiency conversation possible in a domain without prices: without it, budget debates argue about inputs, with it, they argue about what a unit of the service actually costs and whether that unit cost is rising. Its strategic significance is comparability: cost per citizen served across delivery modes (in-person, digital, assisted) is the evidence base for channel-migration and shared-service decisions, and the digital-versus-traditional gap is the standard business case for government digital programs. The honest construction is careful about the denominator: citizens served versus transactions served differ by repeat-use patterns, and services with heavy repeat users look cheaper on the transaction basis. Read with service-quality and access-equity data, since a cost-per-citizen improvement achieved by serving fewer citizens is rationing wearing efficiency's clothes.

## Formula

```
CPCS = Total Service Delivery Cost / Citizens Served
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** organization
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** public_sector_government
- **Sector:** public_sector

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 633 (batch 2)
