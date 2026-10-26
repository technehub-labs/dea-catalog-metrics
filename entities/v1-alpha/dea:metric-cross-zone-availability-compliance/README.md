# dea:metric-cross-zone-availability-compliance

Candidate Performance Metric record for **Cross-Zone Availability Compliance** (CZAC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cross-zone-availability-compliance`
- **Name:** Cross-Zone Availability Compliance
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CZAC

## 2. Definition

Within Data Centers & Cloud Infrastructure, Cross-Zone Availability Compliance (CZAC) is used to gauge exposure to adverse outcomes. Its calculation is Services Meeting Zone Redundancy Standard / Services, measured in percent (%). It originates from and is most used in Technology practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures whether customer workloads comply with availability-zone resilience requirements - multi-zone distribution of critical components. The hard lesson of cloud operations is that resilience is the customer's architecture and the provider's zones: compliance exposure is mutual, and outage post-mortems repeatedly find single-zone deployments customers believed were redundant. Audit sampled topologies, not attestations. Read with zone-level incident history and customer architecture guidance adherence.

## Formula

```
Services Meeting Zone Redundancy Standard / Services
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** data_centers_cloud_infrastructure
- **Sector:** technology

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2147 (batch 6)
